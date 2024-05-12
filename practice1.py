from urllib.request import urlretrieve
from zipfile import ZipFile
import os
from IPython.display import Image
import cv2
import matplotlib.pyplot as plt

# def download_and_unzip(url, save_path):
#     print('Downloading and extracting')
#     urlretrieve(url, save_path)
#
#     try:
#         with ZipFile(save_path) as z:
#             z.extractall(path=os.path.split(save_path)[0])
#         print("Done")
#     except Exception as ex:
#         print("Invalid", ex)


# asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp.zip")
# if not os.path.exists(asset_zip_path):
#     download_and_unzip("https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1", asset_zip_path)

# Image(filename="checkerboard_18x18.png")


# reading images using OpenCV
# cb_img = cv2.imread("../unzip_folder/checkerboard_18x18.png", 0)
# print(cb_img)
#
# # display image attibutes
# # print the size of image
# print("Image size (H, W) is: ", cb_img.shape)
#
# # print data type of image
# print("Data type of image is: ", cb_img.dtype)

# display images using Matplotlib
# plt.imshow(cb_img)
# plt.show()

# plt.imshow(cb_img, cmap="gray")
# plt.show()

# cb_img_fuzzy = cv2.imread("../unzip_folder/checkerboard_fuzzy_18x18.jpg", 0)
# print(cb_img_fuzzy)
# plt.imshow(cb_img_fuzzy, cmap="gray")
# plt.show()

# img = cv2.imread("../unzip_folder/coca-cola-logo.png")
# plt.imshow(img)
# plt.show()

# Image("coca-cola-logo.png")


# coke_img = cv2.imread("../unzip_folder/coca-cola-logo.png", 1)
# print("Image size (H, W, C) is: ", coke_img.shape)

# load a color image
# img_color = cv2.imread("../unzip_folder/coca-cola-logo.png", cv2.IMREAD_COLOR)
# img_color = cv2.imread("../unzip_folder/coca-cola-logo.png", cv2.IMREAD_GRAYSCALE)
#
# plt.imshow(img_color)
# plt.show()

# converting to different color spaces




