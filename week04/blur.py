import cv2 as cv  

img = cv.imread('week04\superman.jpg')
#.GaussianBlur() = blur function
blurred = cv.GaussianBlur(img, (5, 5), 0)
# Kernal = only odd num sizing of img for blur
# 0  = rubbing

# .Canny() =drawing line value between color conflict
edges = cv.Canny(blurred, 10, 150)

cv.imshow('Blurred', blurred)
cv.imshow('Edges', edges)
cv.waitKey(0)