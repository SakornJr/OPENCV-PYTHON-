import cv2 as cv

img = cv.imread('imgs\IMAGE.jpg')

#resize
#.resize
#.resize() = 1. img(input) 2. (width), (height) unit: px
img_resize = cv.resize(img, (300 ,450))

cv.imshow('resize', img_resize)
cv.waitKey(0)
cv.destroyAllWindows