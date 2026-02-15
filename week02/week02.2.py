import cv2 as cv

img = cv.imread('imgs\IMAGE.jpg')

if img is None:
    print("Picture not Found")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
# cvt = convert

cv.imshow('Result', gray)
cv.waitKey(0)
cv.destroyAllWindows