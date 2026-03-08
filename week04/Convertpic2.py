#HSV
import cv2 as cv
#import numpy for using calcultate numberic code color
import numpy as np
img = cv.imread('week04\superman.jpg')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# tone of blue

lower_blue = np.array([100, 50 , 50])

upper_blue = np.array([130, 255, 255])
#Set tone blue lower and upper for mask
#.array() = storing a value color(RGB)
#mask
#.inRange() = range value of color
mask = cv.inRange(hsv, lower_blue, upper_blue)
#.bitwise_and() = merge the image
result = cv.bitwise_and(img, img , mask=mask)

cv.imshow('Original', img)
cv.imshow('mask', mask)
cv.imshow('Result', result)

cv.waitKey(0)