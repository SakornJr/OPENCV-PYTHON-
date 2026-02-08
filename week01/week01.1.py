import cv2
# function ตามด้วยวงเล็บ
image = cv2.imread('imgs\IMAGE.jpg')

# save an image
# .imwrite() includeing with 2 parameter 1. new name of file 2. image
save_image = cv2.imwrite('new2.jpeg', image)

newFile = cv2.imread('new2.jpeg')

cv2.imshow('test', newFile)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Module or Library named OpenCV as cv2


#function in cv2
#.imread()
#.imwrite()
#.imshow()
#.waitKey()
#.destroyAllWindows()
