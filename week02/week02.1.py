import cv2 as cv
# open cam from your device
cap = cv.VideoCapture(0)

if not cap.read():
    print("Can't open cam")
    
while True: 
    res, frame = cap.read()
    
    if not res:
        print("Can't recieve frame exiting")
        break 
      
    cv.imshow("My cam", frame)
    
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows    