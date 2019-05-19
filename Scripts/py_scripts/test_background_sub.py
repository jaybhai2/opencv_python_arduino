import cv2
import numpy as numpy
import time
capture = cv2.VideoCapture("C:\\users\\jweif\\Documents\\highway.mp4")

_, first_frame = capture.read()
while True:
    _, frame = capture.read()    # read return a tuple to be unpacked into _ thorw away variable and frame. 
    deltaFrame = cv2.absdiff(first_frame,frame)   
    
    
    
    #cv2.imshow("FirstFrame", first_frame)
    #cv2.imshow("Highway",frame)

    cv2.imshow("deltaFrame",deltaFrame)


    key = cv2.waitKey(30)

    frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    #print(str(type(frameWidth)) +" " + str(frameWidth))
    time.sleep(1)


    pixel = deltaFrame[100,100]
    #print (pixel, end=" ")

    if key == 27:
        break
    #print(cv2.getWindowProperty('Highway',cv2.WND_PROP_VISIBLE))
        
time.sleep(1)
#print(cv2.getWindowProperty('Highway',cv2.WND_PROP_VISIBLE))
capture.release()
cv2.destroyWindow("Highway")
