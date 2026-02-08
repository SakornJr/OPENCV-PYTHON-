# เรียกใช้ module OpenCV as cv2
import cv2

# กำนหด ตัวแปรรับค่าที่เรียกใช้ module cv2 function .imread()
# .imread() = อ่านรูป และ ใน function('path of an image')
image = cv2.imread('imgs\IMAGE.jpg')
# .imshow() = โชว์รูป
# .imshow(label ของ program, รูปตัวแปร)
cv2.imshow('Diddy Oil', image)
# .waitKey() = รอ program.....
# 0 แปลว่ากดปุ่มไหนก็ได้

cv2.waitKey(0)

# ปิดโปรแกรม
cv2.destroyAllWindows