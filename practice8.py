import glob
import math

from common_function import download_and_unzip
import os
import cv2
from matplotlib import pyplot as plt

# download_and_unzip('https://www.dropbox.com/s/0o5yqql1ynx31bi/opencv_bootcamp_assets_NB9.zip?dl=1',
#                    '../unzip_folder8/bootcamp_opencv.zip')

imageFiles = glob.glob(f'../unzip_folder8/boat/*')
imageFiles.sort()

images = []
for imageFile in imageFiles:
    img = cv2.imread(imageFile)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

num_images = len(images)
plt.figure()
num_columns = 3
num_rows = math.ceil(num_images / num_columns)

# for i in range(num_images):
#     plt.subplot(num_rows, num_columns, i + 1)
#     plt.imshow(images[i])
#
# plt.show()


# stitcher
stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images)
if status == 0:
    plt.figure()
    plt.imshow(result)
    plt.show()
