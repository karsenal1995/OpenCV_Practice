import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from zipfile import ZipFile
from urllib.request import urlretrieve
import os


# def download_and_extract(url, save_file_path):
#     print("Start downloading...")
#     urlretrieve(url, save_file_path)
#     try:
#         with ZipFile(save_file_path, 'r') as zip:
#             zip.extractall(os.path.split(save_file_path)[0])
#         print("Done")
#     except Exception as ex:
#         print("Invalid: ", ex)
#
#
# file_path = os.path.join(os.getcwd(), "../unzip_folder7/bootcamp_opencv.zip")
# download_and_extract("https://www.dropbox.com/s/zuwnn6rqe0f4zgh/opencv_bootcamp_assets_NB8.zip?dl=1", file_path)


# Read template and scanned image
im1 = cv2.imread("../unzip_folder7/form.jpg", cv2.IMREAD_COLOR)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

im2 = cv2.imread("../unzip_folder7/scanned-form.jpg", cv2.IMREAD_COLOR)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

# plt.figure()
# plt.subplot(121)
# plt.imshow(im1)
# plt.title("Original Image")
#
# plt.subplot(122)
# plt.imshow(im2)
# plt.title("Scanned Image")
#
# plt.show()

im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# detect ORB features and compute keypoints
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, description1 = orb.detectAndCompute(im1_gray, None)
keypoints2, description2 = orb.detectAndCompute(im2_gray, None)

im1_display = cv2.drawKeypoints(im1, keypoints1, outImage=np.array([]), color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
im2_display = cv2.drawKeypoints(im2, keypoints2, outImage=np.array([]), color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# plt.figure()
# plt.subplot(121)
# plt.imshow(im1_display)
# plt.title('Original Image')
#
# plt.subplot(122)
# plt.imshow(im2_display)
# plt.title('Scanned Image')
#
# plt.show()

# Match keypoints
print(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE)

matchers = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE)
matches = list(matchers.match(description1, description2, None))
matches.sort(key=lambda x: x.distance, reverse=False)
numGoodMatches = int(len(matches) * 0.1)
matches = matches[:numGoodMatches]
im_matches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
# plt.figure()
# plt.title('Original Image')
# plt.imshow(im_matches)
# plt.show()

# Find homography
points1 = np.zeros((len(matches), 2), dtype="float32")
points2 = np.zeros((len(matches), 2), dtype="float32")
for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt # queryIdx, trainIdx
    points2[i, :] = keypoints2[match.trainIdx].pt

h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

# Warp image
height, width, channels = im1.shape
im2_reg = cv2.warpPerspective(im2, h, (width, height))
# plt.figure()
# plt.subplot(121)
# plt.title('Original Image')
# plt.axis("off")
# plt.imshow(im1)
#
# plt.subplot(122)
# plt.title('Matched Image')
# plt.axis("off")
# plt.imshow(im2_reg)
#
# plt.show()