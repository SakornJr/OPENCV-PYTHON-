#why use grayscale 
# use less time
import cv2 as cv


img = cv.imread('imgs\IMAGE.jpg')

if img is None:
    print('Cloud not found read the images.')

# gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

saveNew = cv.imwrite('grayscale.jpeg', gray)
newFile = cv.imread('grayscale.jpeg')

cv.imshow('GrayScale', gray)
cv.waitKey(0)
cv.destroyAllWindows()