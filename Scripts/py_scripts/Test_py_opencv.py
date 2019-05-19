import cv2, time
import serial
import numpy as np


print("Starting object detection...")
time.sleep(2)

vd = cv2.VideoCapture(1)  #0 denote first camera. if video file, input path

print("Webcam opened.")
print("First frame capture in 3 seconds.")


bkg_frame = None

width = vd.get(cv2.CAP_PROP_FRAME_WIDTH )
height = vd.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  vd.get(cv2.CAP_PROP_FPS)
print(str(width) + ' ' + str(height)+ ' ' + str(fps))
time.sleep(2)

subtract = cv2.createBackgroundSubtractorMOG2(history = 20,varThreshold=60)
while True:

    check, frame = vd.read()

    diff_frame = subtract.apply(frame)

    '''
    print(check)
    cur_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cur_frame = cv2.GaussianBlur(cur_frame,(21,21),0)

    if bkg_frame is None:
        bkg_frame = cur_frame
        continue

    diff_frame = cv2.absdiff(bkg_frame, cur_frame)
    '''
    _,diff_frame_threshold = cv2.threshold(diff_frame, 50, 255, cv2.THRESH_BINARY) # filter out all <30 from diff_frame

    diff_frame_threshold = cv2.dilate(diff_frame_threshold, None, iterations=2)
    
    
    _,contours,_ = cv2.findContours(diff_frame_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        boxArea = cv2.contourArea(contour)
        if boxArea < 300: #pixel
           continue
        
        (x,y,w,h) = cv2.boundingRect(contour)
    
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        areaStr = str(boxArea)
        cv2.putText(frame, areaStr, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), lineType=cv2.LINE_AA) 
   

    cv2.imshow("different_frame",diff_frame)
    cv2.resizeWindow('different_frame', 600,600)
    cv2.imshow("frame",frame)

    #print(diff_frame_threshold)
    time.sleep(0.1)    
    key=cv2.waitKey(1)
    print(key)
    if key == ord('q'):
        break    

vd.release()
cv2.destoryAllWindows
