import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from zipfile import ZipFile
from urllib.request import urlretrieve
from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode

# def download_and_unzip(url, path):
#     print("Downloading", url)
#     urlretrieve(url, path)
#     try:
#         with ZipFile(path, 'r') as zip:
#             zip.extractall(os.path.split(path)[0])
#
#         print("Done")
#     except Exception as ex:
#         print("Error", ex)
#
#
# url_path = os.path.join(os.getcwd(), "../unzip_folder5/bootcamp_opencv.zip")
# if not os.path.exists(url_path):
#     download_and_unzip("https://www.dropbox.com/s/p8h7ckeo2dn1jtz/opencv_bootcamp_assets_NB6.zip?dl=1", url_path)


cap = cv2.VideoCapture("../unzip_folder5/race_car.mp4")
if not cap.isOpened():
    print("Error opening video")

retval, frame = cap.read()
plt.imshow(frame[..., ::-1])
# plt.show()


video = YouTubeVideo("RwxVEjv78LQ", width=700, height=438)
# display(video)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out_avi = cv2.VideoWriter("../unzip_folder5/result/race_car.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width, frame_height))
out_mp4 = cv2.VideoWriter("../unzip_folder5/result/race_car.mp4", cv2.VideoWriter_fourcc(*"XVID"), 10, (frame_width, frame_height))

while cap.isOpened():
    retval, frame = cap.read()
    if retval:
        out_avi.write(frame)
        out_mp4.write(frame)
    else:
        break

cap.release()
out_avi.release()
out_mp4.release()