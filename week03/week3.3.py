import cv2 as cv 
#Library Numpy using for handle array or list in python or calculate multi dimesion
# Numpy was so good at hight calculation about com Sci
import numpy as np


#paper
# np.zeros() = 1 size of paper (height), (width) 2. primary color (RGB)
img = np.zeros((400 , 600, 3))

#Horizontal

for x in range(0, 600, 100):
    #.line() = 1. paper 2. point1 3. point2 4. color 5. line bold
    cv.line(img, (x, 0), (x, 400), (39, 245, 46), 10)
    
    
# Vertical    
for y in range(0, 400, 100):
    cv.line(img, (0,y), (600, y), (39, 245, 46), 10) 
    
    
# Draw a square (center) table
x1, y1 = 200, 100
x2, y2 = 400, 300

# Drawing a rectangle
#. rectangle() = 1. img (paper) 2. ROI 
cv.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 5)       

#Text
# .putText() = 1 img 2 message(str) 3 ROI 4 font 5 fontsize 6 color 7 bold

cv.putText(img, 'My ROI Area', (210, 90) , cv.FONT_HERSHEY_SIMPLEX, 0.8, (46, 245, 39), 5)

#crop ROI
roi_img = img[y1:y2 , x1:x2]

#show result

cv.imshow('Main image', img)

cv.imshow('cropped ROI ', roi_img)

cv.waitKey(0)
cv.destroyAllWindows


 