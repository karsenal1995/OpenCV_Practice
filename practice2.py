import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve
from IPython.display import Image


# def download_and_unzip(url, save_path):
#     print("downloading and extracting assests: ")
#     urlretrieve(url, save_path)
#     try:
#         with ZipFile(save_path) as z:
#             z.extractall(os.path.split(save_path)[0])
#         print("Done")
#     except Exception as ex:
#         print("Invalid file, ", ex)
#
#
# file_path = os.path.join(os.getcwd(), "../unzip_folder2/opencv_bootcamp.zip")
# if not os.path.exists(file_path):
#     download_and_unzip("https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1", file_path)


# cb_img = cv2.imread("../unzip_folder2/checkerboard_18x18.png", cv2.IMREAD_GRAYSCALE)
# print(cb_img)
# plt.imshow(cb_img, cmap="gray")
# plt.show()

# cb_img_copy = cb_img.copy()
# cb_img_copy[2, 2] = 200
# cb_img_copy[2, 3] = 200
# cb_img_copy[3, 2] = 200
# cb_img_copy[3, 3] = 200
# plt.imshow(cb_img_copy, cmap="gray")
# plt.show()

# cropping images
img_NZ_bgr = cv2.imread("../unzip_folder2/New_Zealand_Lake.jpg", 1)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]
# plt.imshow(img_NZ_rgb)
# plt.show()

cropped_region = img_NZ_rgb[450:550, 300:500]
# plt.imshow(cropped_region)
# plt.show()

# Method 1: Specifying scaling factor using fx, fy
# resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)
# plt.imshow(resized_cropped_region_2x)
# plt.show()

# Method 2: Specifying exact size of the output image
resized_cropped_region = cv2.resize(cropped_region, dsize=(100, 200), interpolation=cv2.INTER_AREA)
# plt.imshow(resized_cropped_region)
# plt.show()

cv2.imwrite("../unzip_folder2/result/resize_cropped.jpg", resized_cropped_region)
Image(filename="../unzip_folder2/result/resize_cropped.jpg")


# Flipping images
img = cv2.imread("../unzip_folder2/coca-cola-logo.png", 1)
# swap order channel
img_swap = img[:, :, ::-1]
img_swap_flipped_horizontal = cv2.flip(img_swap, 1)
img_swap_flipped_vertical = cv2.flip(img_swap, 0)
img_swap_flipped_both = cv2.flip(img_swap, -1)

plt.figure(figsize=(18, 5))
plt.subplot(141)
plt.imshow(img_swap_flipped_horizontal)
plt.title("Horizontal flip")
# plt.show()

plt.subplot(142)
plt.imshow(img_swap_flipped_vertical)
plt.title("Vertical flip")
# plt.show()

plt.subplot(143)
plt.imshow(img_swap_flipped_both)
plt.title("Both flip")
# plt.show()

plt.subplot(144)
plt.imshow(img_swap)
plt.title("Original")
plt.show()



