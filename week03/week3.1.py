import cv2 as cv 

img = cv.imread('imgs\IMAGE.jpg')

#Flip
#.flip() = 1. img (input) 2. 1(left - right) 0:(up or down)
                                     
img_flip = cv.flip(img, 1 )

cv.imshow('Flip', img_flip)
cv.waitKey(0)
cv.destroyAllWindows
