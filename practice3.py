import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from zipfile import ZipFile
from urllib.request import urlretrieve


# def download_and_unzip(url, save_path):
#     print("Start downloading...")
#     urlretrieve(url, save_path)
#     try:
#         with ZipFile(save_path) as zip_file:
#             zip_file.extractall(os.path.split(save_path)[0])
#         print("Done")
#     except Exception as ex:
#         print("Invalid: ", ex)
#
#
# assets_zip_path = os.path.join(os.getcwd(), "../unzip_folder3/opencv_bootcamp.zip")
# if not os.path.exists(assets_zip_path):
#     download_and_unzip("https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1", assets_zip_path)


img = cv2.imread("../unzip_folder3/New_Zealand_Boat.jpg", 1)
# plt.imshow(img[:, :, ::-1])
# plt.show()

# Drawing a line
# img_line = img.copy()
# cv2.line(img_line, (300, 100), (500, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
# plt.imshow(img_line[:, :, ::-1])
# plt.show()

# Drawing a circle
# img_circle = img.copy()
# cv2.circle(img_circle, (450, 250), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)
# plt.imshow(img_circle[:, :, ::-1])
# plt.show()

# Drawing a Rectangle
img_rectangle = img.copy()
cv2.rectangle(img_rectangle, (350, 200), (500, 350), (255, 0, 255), thickness=5, lineType=cv2.LINE_AA)
plt.imshow(img_rectangle[:, :, ::-1])
plt.show()

# Adding text
# img_text = img.copy()
# text = "Boat"
# fontFace = cv2.FONT_HERSHEY_SIMPLEX
# fontScale = 2.3
# fontColor = (0, 255, 0)
# fontThickness = 2
# cv2.putText(img_text, text, (350, 400), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
# plt.imshow(img_text[:, :, ::-1])
# plt.show()