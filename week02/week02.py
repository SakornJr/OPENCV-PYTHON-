# as mean set module to new name

import cv2 as im_vid

cap = im_vid.VideoCapture('Video\meme2.mp4')




while True:
    res, frame = cap.read()
    
    if not res:
        print('Not found the video')
        break
    
    im_vid.imshow('Meme', frame)
    
    # press q to quit
    if im_vid.waitKey(1) == ord('q'):
        break
#cv2.waitKey(0) press any button for...

#output the image capture from video    
cap.release()
im_vid.destroyAllWindows()
        