# Haarcasecade
# it is file for classification face
import cv2 as cv

# 1) loading file haar casecade
cascade_path = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'

face_casecade = cv.CascadeClassifier(cascade_path)

if face_casecade.empty():
    print('Loading file Haarcasecade fail')
    exit()
    
# 2) Load image
img = cv.imread('pictures\Real Prime team.jpg')

if img is None:
    print('Image not found')
    exit()

# 3) Convert RGB to GrayScale
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    


# 4) Face detection
face = face_casecade.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=5,minSize=(30,30))
#.detectMultiScale() = detection object
# if the object is near camera => Big face
# if the object is far camera => Small face
# gray_scale, Standard image covert to gray
#scaleFactor=1.1 Scan face to reduce the size
#minNeighbors=5 Should believe this area to real face (5 round)
#minSize=(30,30) Interseted the object at least 30*30 pixels in size


print(f'Face found{len(face)}')


# 5) Drawing frame if detected 
for (x, y, w, h ) in face:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2 )

# 6 show result    

cv.imshow('Face Detection in Image', img)
cv.waitKey(0)
cv.destroyAllWindows