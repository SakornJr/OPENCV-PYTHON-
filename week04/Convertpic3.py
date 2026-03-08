import cv2 as cv 
import numpy as np  
import matplotlib.pyplot as plt

#matplotlib.pyplot = create a graph, create table

img = cv.imread('week04\superman.jpg')

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)




grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayscale_3inch = cv.cvtColor(img, cv.COLOR_GRAY2RGB)


img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

mask = cv.inRange(img_hsv, lower_red, upper_red)

color_part = cv.bitwise_and(img_rgb, img_rgb, mask=mask)

grayscale_part = cv.bitwise_and(grayscale_3inch, grayscale_3inch, mask=cv.bitwise_not(mask))

final_image = cv.add(color_part, grayscale_part)

cv.imshow('RGB', img_rgb)
cv.imshow('Grayscale', grayscale)
cv.imshow('3inch', grayscale_3inch)
cv.imshow('HSV', img_hsv)
cv.imshow('Colorpart', color_part)
cv.imshow('gray scale part', grayscale_part)

plt.imshow(final_image)
plt.title('Color splash: RED ONLY!')
plt.show()