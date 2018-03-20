#!/usr/bin/python3
import cv2
from matplotlib import pyplot as plt
import numpy as np

# Read
img = cv2.imread("glitter-pink-original.jpg")
img2 = cv2.imread("glitter-pink.jpg")
bwimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
bwimg2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Approximate the blur
gsize = (61, 61)
img = cv2.GaussianBlur(img, gsize, 0)
bwimg = cv2.GaussianBlur(bwimg, gsize, 0)

# Do some diffing.
chan = [0]
hist = cv2.calcHist([bwimg], chan, None, [256], [0,256])
hist2 = cv2.calcHist([bwimg2], chan, None, [256], [0,256])
diff = cv2.absdiff(img2, img)

# Gamma correction
gamma = 1.6
# img.convertTo(imgFloat, cv2.CV_32F)
imgFloat = np.float32(img)
channels = cv2.split(imgFloat)
for i in range(len(channels)):
    channels[i] = channels[i] / 255.0
    channels[i] = cv2.pow(channels[i], gamma)
    channels[i] = channels[i] * 255.0
    channels[i] = np.uint8(channels[i])
corrected8U = cv2.merge(channels)

# Show
cv2.namedWindow("original", cv2.WINDOW_AUTOSIZE)
cv2.imshow("original", img)
cv2.namedWindow("correct", cv2.WINDOW_AUTOSIZE)
cv2.imshow("correct", img2)
# cv2.namedWindow("origbw", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("origbw", bwimg)
# cv2.namedWindow("correctbw", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("correctbw", bwimg2)
# cv2.namedWindow("diff", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("diff", diff)
cv2.namedWindow("corrected", cv2.WINDOW_AUTOSIZE)
cv2.imshow("corrected", corrected8U)
# plt.subplot(311), plt.imshow(img)
# plt.subplot(312), plt.imshow(img2)
# plt.subplot(313),
# plt.plot(hist), plt.plot(hist2)
# plt.xlim([0, 256])
# plt.show()

# Event loop
cv2.waitKey(0)
cv2.destroyAllWindows()
