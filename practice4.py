import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve
#
#
# # def download_and_unzip(url, save_path):
# #     print("Downloading")
# #     urlretrieve(url, save_path)
# #     try:
# #         with ZipFile(save_path) as zip:
# #             zip.extractall(os.path.split(save_path)[0])
# #         print("Done")
# #     except Exception as e:
# #         print("invalid: ", e)
# #
# #
# # zip_path = os.path.join(os.getcwd(), "../unzip_folder4/bootcamp_opencv.zip")
# # if not os.path.exists(zip_path):
# #     download_and_unzip("https://www.dropbox.com/s/0oe92zziik5mwhf/opencv_bootcamp_assets_NB4.zip?dl=1", zip_path)
#
# # Original image
# # img_bgr = cv2.imread('../unzip_folder4/New_Zealand_Coast.jpg', cv2.IMREAD_COLOR)
# # img_rbg = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# # plt.imshow(img_rbg)
# # plt.show()
# #
# # # Additional or brightness
# # matrix = np.ones(img_rbg.shape, dtype="uint8") * 50
# # img_rbg_brighter = cv2.add(img_rbg, matrix)
# # img_rbg_darker = cv2.subtract(img_rbg, matrix)
# # plt.figure(figsize=[18, 5])
# #
# # plt.subplot(131)
# # plt.imshow(img_rbg_brighter)
# # plt.title("Brighter Image")
# #
# # plt.subplot(132)
# # plt.imshow(img_rbg)
# # plt.title("Original Image")
# #
# # plt.subplot(133)
# # plt.imshow(img_rbg_darker)
# # plt.title("Darker Image")
# #
# # plt.show()
#
# # Multiplication or contrast
# # matrix1 = np.ones(img_rbg.shape) * 0.8
# # matrix2 = np.ones(img_rbg.shape) * 1.2
# # img_rbg_darker = np.uint8(cv2.multiply(np.float64(img_rbg), matrix1))
# # # img_rbg_brighter = np.uint8(cv2.multiply(np.float64(img_rbg), matrix2))
# # # handle overflow by np.clip
# # img_rbg_brighter = np.uint8(np.clip(cv2.multiply(np.float64(img_rbg), matrix2), 0, 255))
#
#
# # plt.figure()
# # plt.subplot(131)
# # plt.imshow(img_rbg_darker)
# # plt.title("Darker image")
# #
# # plt.subplot(132)
# # plt.imshow(img_rbg)
# # plt.title("Original image")
# #
# # plt.subplot(133)
# # plt.imshow(img_rbg_brighter)
# # plt.title("Brighter image")
# #
# # plt.show()
#
#
# # img_read = cv2.imread("../unzip_folder4/building-windows.jpg", cv2.IMREAD_GRAYSCALE)
# # retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)
# #
# # plt.figure()
# # plt.subplot(121)
# # plt.imshow(img_thresh, cmap="gray")
# # plt.title("Threshhold image")
# #
# # plt.subplot(122)
# # plt.imshow(img_read, cmap="gray")
# # plt.title("Original image")
# #
# # plt.show()
# # print(img_thresh.shape)
#
# # # Image Thresholding
# # img_read = cv2.imread("../unzip_folder4/Piano_Sheet_Music.png", 0)
# # retval1, img_thresh_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)
# # retval2, img_thresh_2 = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)
# # img_adapt_thresh = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)
# # plt.figure()
# #
# # plt.subplot(221)
# # plt.title("Original Image")
# # plt.imshow(img_read, cmap="gray")
# #
# # plt.subplot(222)
# # plt.title("Threshold 50")
# # plt.imshow(img_thresh_1, cmap="gray")
# #
# # plt.subplot(223)
# # plt.title("Threshold 130")
# # plt.imshow(img_thresh_2, cmap="gray")
# #
# # plt.subplot(224)
# # plt.title("Adaptive threshold")
# # plt.imshow(img_adapt_thresh, cmap="gray")
# #
# # plt.show()
#
#
# # # Bitwise operating
# img_rec = cv2.imread('../unzip_folder4/rectangle.jpg', cv2.IMREAD_GRAYSCALE)
# img_circle = cv2.imread('../unzip_folder4/circle.jpg', cv2.IMREAD_GRAYSCALE)
#
# # AND operating
# # black + black = black, white + white = white
# # black + white = black
#
# # result = cv2.bitwise_and(img_rec, img_circle, mask=None)
# # plt.imshow(result, cmap="gray")
# # plt.show()
#
# # OR operating
# # same color dont change
# # black + white = white
#
# # result = cv2.bitwise_or(img_rec, img_circle, mask=None)
# # plt.imshow(result, cmap="gray")
# # plt.show()
#
#
# # XOR operating
# # 0: black, 1: white
# # 0 + 0 = 0
# # 0 + 1 = 1 + 0 = 1
# # 1 + 1 = 0
#
# # result = cv2.bitwise_xor(img_rec, img_circle)
# # plt.imshow(result, cmap="gray")
# # plt.show()
#
# # NOT operating
# # result = cv2.bitwise_not(img_rec, img_circle)
# # plt.imshow(result, cmap="gray")
# # plt.show()
#
#
# img_bgr = plt.imread('../unzip_folder4/coca-cola-logo.png')
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# # plt.imshow(img_bgr)
# # # plt.show()
# #
# # logo_w = img_rgb.shape[0]
# # log_h = img_rgb.shape[1]
# #
# # img_background_bgr = plt.imread('../unzip_folder4/checkerboard_color.png')
# # img_background_rbg = cv2.cvtColor(img_background_bgr, cv2.COLOR_BGR2RGB)
# # aspect_ratio = logo_w/(img_background_rbg.shape[1])
# # dim = (logo_w, int(aspect_ratio * img_background_rbg.shape[0]))
# #
# # # Resize img_background_rbg
# # img_background_rbg = cv2.resize(img_background_rbg, dim, interpolation=cv2.INTER_AREA)
# # plt.imshow(img_background_rbg)
# # plt.show()
#
# # Create mask for original image
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
# # plt.imshow(img_gray, cmap='gray')
# # plt.show()
#
# retval, img_mask = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
# plt.imshow(img_mask, cmap='gray')
# plt.show()
#
# # img_mask_inv = cv2.bitwise_not(img_gray)
# # plt.imshow(img_mask_inv, cmap='gray')
# # plt.show()


img_bgr = cv2.imread("../unzip_folder4/coca-cola-logo.png")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
retval, img_mask = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# plt.imshow(img_mask, cmap="gray")
# plt.show()

img_mask_inv = cv2.bitwise_not(img_mask)
# plt.imshow(img_mask_inv, cmap="gray")
# plt.show()

img_background_bgr = cv2.imread("../unzip_folder4/checkerboard_color.png")
img_background_rgb = cv2.cvtColor(img_background_bgr, cv2.COLOR_BGR2RGB)

# Set desired width (logo_w) and maintain image aspect ratio
logo_w = img_rgb.shape[0]
logo_h = img_rgb.shape[1]
aspect_ratio = logo_w / img_background_rgb.shape[1]
dim = (logo_w, int(img_background_rgb.shape[0] * aspect_ratio))
img_background_rgb = cv2.resize(img_background_rgb, dim, interpolation=cv2.INTER_AREA)

img_background = cv2.bitwise_and(img_background_rgb, img_background_rgb, mask=img_mask)
# plt.imshow(img_background)
# plt.show()

img_foreground = cv2.bitwise_and(img_rgb, img_rgb, mask=img_mask_inv)
# plt.imshow(img_foreground, cmap="gray")
# plt.show()

# Merge
result = cv2.add(img_background, img_foreground)
plt.imshow(result)
cv2.imwrite("../unzip_folder4/result/logo_final.png", result[:, :, ::-1])
plt.show()


# =============  Bitwise operating ==================== #
# AND operating is a multiply
# 1001 AND 0001 = 0001 (1 * 0, 0 * 0, 0 * 0, 1 * 1)

# OR operating is an add
# 1001 AND 0001 = 1001 (1 + 0, 0 + 0, 0 + 0, 1 + 1 = 1)

# XOR operating is an add
# 1001 AND 0001 = 1000 (1 + 0, 0 + 0, 0 + 0, 1 + 1 = 0)