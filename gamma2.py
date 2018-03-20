#!/usr/bin/python3
import cv2
import numpy as np
import glob

images = glob.glob("orig/*.jpg")
for filename in images:
    # Read
    img = cv2.imread(filename)

    # Gamma correction
    gamma = 1.6 # for CMG images.

    # img.convertTo(imgFloat, cv2.CV_32F)
    imgFloat = np.float32(img)
    channels = cv2.split(imgFloat)
    for i in range(len(channels)):
        channels[i] = channels[i] / 255.0
        channels[i] = cv2.pow(channels[i], gamma)
        channels[i] = channels[i] * 255.0
        channels[i] = np.uint8(channels[i])
    corrected8U = cv2.merge(channels)

    cv2.imwrite("gam/" + filename[5:], corrected8U)
