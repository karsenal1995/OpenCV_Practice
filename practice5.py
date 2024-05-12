import sys
import cv2

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)
win_name = "Camera preview"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# wait key meaning wait for 1 ms to check if the Esc key has been pressed
while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyAllWindows()