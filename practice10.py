import os.path
from base64 import b64encode
import cv2
import matplotlib.pyplot as plt
import sys
from IPython.display import HTML, YouTubeVideo, display
from common_function import download_and_unzip

# download_and_unzip('https://www.dropbox.com/s/ld535c8e0vueq6x/opencv_bootcamp_assets_NB11.zip?dl=1',
#                    '../unzip_folder10/bootcamp_opencv.zip')

# video = YouTubeVideo("XkJCvtCRdVM", 1024, 640)
# display(video)


def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)


def displayRectangle(frame, bbox):
    plt.figure()
    frameCopy = frame.copy()
    drawRectangle(frameCopy, bbox)
    frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_RGB2BGR)
    plt.imshow(frameCopy)
    plt.axis("off")
    # plt.show()


def drawText(frame, txt, location, color=(50, 170, 50)):
    cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)


track_types = ["BOOSTING", "MIL", "KCF", "CSRT", "TLD", "MEDIANFLOW", "GOTURN", "MOSSE"]
track_type = track_types[1]

match track_type:
    case "BOOSTING":
        tracker = cv2.TrackerBoosting_create()

    case "MIL":
        tracker = cv2.TrackerMIL.create()

    case "KCF":
        tracker = cv2.TrackerKCF_create()

    case "CSRT":
        tracker = cv2.legacy.TrackerCSRT.create()

    case "TLD":
        tracker = cv2.legacy.TrackerTLD.create()

    case "MEDIANFLOW":
        tracker = cv2.legacy.TrackerMedianFlow.create()

    case "GOTURN":
        tracker = cv2.TrackerGOTURN.create()

    case _:
        tracker = cv2.legacy.TrackerMOSSE.create()


video = cv2.VideoCapture("../unzip_folder10/race_car.mp4")
ok, frame = video.read()

if not video.isOpened():
    print("Maybe cant open video")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_output_file_name = "race_car " + track_type + ".mp4"
video_output = cv2.VideoWriter(os.path.join("../unzip_folder10/result", video_output_file_name),
                               cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height), True)

bbox = (1300, 405, 160, 120)
displayRectangle(frame, bbox)

## initialize tracker with first frame and bouding box
ok = tracker.init(frame, bbox)

while True:
    ok, frame = video.read()

    if not ok:
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Drawing bouding box
    if ok:
        drawRectangle(frame, bbox)
    else:
        drawText(frame, "Tracking failure detected", (80, 140), (0, 0, 255))

    # Display info
    drawText(frame, track_type + " Tracker ", (80, 60))
    drawText(frame, "FPS: " + str(int(fps)), (80, 100))

    video_output.write(frame)

video.release()
video_output.release()

# ffmpeg -y -i "C:\Users\x1G10\PycharmProjects\OpenCV_Practice\unzip_folder10\race_car.mp4" -c:v libx264 "C:\Users\x1G10\PycharmProjects\OpenCV_Practice\unzip_folder10\result\race_car_track_x264.mp4"  -hide_banner -loglevel error
mp4 = open("../unzip_folder10/result/race_car_track_x264.mp4", "rb").read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML(f"""<video width=1024 controls><source src="{data_url}" type="video/mp4"></video>""")

video = YouTubeVideo("pk3tmdRX4ww", width=1024, height=640)
display(video)

