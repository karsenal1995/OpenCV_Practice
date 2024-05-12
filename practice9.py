from common_function import download_and_unzip
import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt

# download_and_unzip('https://www.dropbox.com/s/qa1hsyxt66pvj02/opencv_bootcamp_assets_NB10.zip?dl=1',
#                    '../unzip_folder9/bootcamp_unzip.zip')


def readImagesAndTimes():
    # filenames = glob.glob(f'../unzip_folder9/*.jpg')
    filenames = ["../unzip_folder9/img_0.033.jpg", "../unzip_folder9/img_0.25.jpg",
                 "../unzip_folder9/img_2.5.jpg", "../unzip_folder9/img_15.jpg"]
    times = np.array([1/30, 0.25, 2.5, 15], dtype=np.float32)
    images = []
    for fileName in filenames:
        im = cv2.imread(fileName)
        images.append(im)

    return images, times


# Align image with createAlignMTB
images, times = readImagesAndTimes()
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

################### Estimate camera response function  ###################
# Find Camera Response Function (CRF)
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)
# Plot CRF
x = np.arange(256, dtype=np.uint8)
y = np.squeeze(responseDebevec)

# ax = plt.figure()
# plt.title("Calibrated Debevec Response Function")
# plt.xlabel("Measured Pixel value")
# plt.ylabel("Calibrated Intensity")
# plt.xlim([0, 260])
# plt.grid()
# plt.plot(x, y[:, 0], "r", x, y[:, 1], "g", x, y[:, 2], "b")
# plt.show()


################  Merge Exposure into an HDR Image ########################
# Merge images into an HDR linear image
mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)

# Tonemap using Drago's method to obtain 24-bit color image
toneMapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDraco = toneMapDrago.process(hdrDebevec)
ldrDraco = ldrDraco * 3
plt.figure()
plt.imshow(np.clip(ldrDraco, 0, 1))
# cv2.imwrite(f'../unzip_folder9/result/ldr-draco.jpg', 255 * ldrDraco[:, :, ::-1])
# print("Saved ldr-draco.jpg")

# Tonemap using Reinhard's method to obtain 24-bit color image
toneMapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
ldrToneMapReinhard = toneMapReinhard.process(hdrDebevec)
plt.figure()
plt.imshow(np.clip(ldrToneMapReinhard, 0, 1))
# cv2.imwrite('../unzip_folder9/result/ldr-draco-reinhard.jpg', ldrToneMapReinhard * 255)
# print("Saved ldr-draco-reinhard.jpg")

# Tonemap using Mantiuk's method to obtain 24-bit color image
toneMapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
ldrToneMapMantiuk = toneMapMantiuk.process(hdrDebevec)
ldrToneMapMantiuk *= 3
plt.figure()
plt.imshow(np.clip(ldrToneMapMantiuk, 0, 1))
cv2.imwrite('../unzip_folder9/result/ldr-draco-mantiuk.jpg', ldrToneMapMantiuk * 255)
print('Saved ldr-draco-mantiuk.jpg')

