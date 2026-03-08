#HSV
import cv2 as cv
import numpy as np
img = cv.imread('week04\superman.jpg')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# tone of blue

lower_blue = np.array([100, 50 , 50])

upper_blue = np.array([130, 255, 255])

#mask
#.inRange() = range value of color
mask = cv.inRange(hsv, lower_blue, upper_blue)

result = cv.bitwise_and(img, img , mask=mask)

cv.imshow('Original', img)
cv.imshow('mask', mask)
cv.imshow('Result', result)

cv.waitKey(0)