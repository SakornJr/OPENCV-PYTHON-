#color , convert image

#RGB = red green blue
#255 , 255 , 255
#HSV = Hue (tone of color) Staturation(vibrancy) Value(Brightness)
#rgb vs hsv
#rgb = can check only one color
#hsv = can check tone or vibrancy its multi color
#crtl shift p select intreupteor
import cv2 as cv




img = cv.imread('week04\superman.jpg')

# we can check just only red color in the image

# Bit Binary(0(black), 1(white))

if img is None:
    print('Cloud not found read the images.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


_, mask = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

result = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Original', img)
cv.imshow('Gray', gray)
cv.imshow('Mask', mask)
cv.imshow('result', result)
cv.waitKey(0)
# cv2.destroyAllWindows