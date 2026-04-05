import cv2 as cv

face_casecade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')



cap = cv.VideoCapture(0)

if not cap.read():
    print('Cannot open the camera')

while True:
    res, frame = cap.read()

    if not res:
        print('Canot receive frame exiting.....')
        break
    #Optimization
    gray_scale = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    #Detect faces 
    face = face_casecade.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=10,minSize=(30,30))

    
    #Draw rectangle
    for (x, y, w, h ) in face:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0,255,0), 2 )
        
       
    cv.imshow('My camera', frame)
    print(f'Face found{len(face)}')

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()