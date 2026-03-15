import cv2 as cv 

img = cv.imread('imgs\IMAGE.jpg')

# width / 2 
# height / 2

height, width = img.shape[:2]
center = (width // 2, height // 2)


#.getRotationMatrix2D = 1. center (formula center) 2. degree 3. scale
angle = cv.getRotationMatrix2D(center, 90, 1.0)

img_rotate = cv.warpAffine(img, angle, (width, height))

cv.imshow('Rotated', img_rotate)
cv.waitKey(0)
cv.destroyAllWindows