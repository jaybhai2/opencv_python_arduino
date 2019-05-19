
#Final
import cv2, time
import serial
import numpy as np
# img = cv2.imread(r'C:\Users\jay\Pictures\Capture.PNG')
# print(type(img))
# print(img)
# print(img.shape)

fdeviation = 0
fthreshold = 10

print("Starting object detection...")
time.sleep(2)

vd = cv2.VideoCapture(1)  #0 denote first camera. if video file, input path

print("Webcam opened.")
print("First frame capture in 3 seconds.")

# _, frame0 = vd.read()
# frame0gray = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
# frame = cv2.GaussianBlur(gray0,(21,21),0)

detectBox =[]
bkg_frame = None

width = vd.get(cv2.CAP_PROP_FRAME_WIDTH )
height = vd.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  vd.get(cv2.CAP_PROP_FPS)
print(str(width) + ' ' + str(height)+ ' ' + str(fps))
time.sleep(2)

subtract = cv2.createBackgroundSubtractorMOG2(history = 20,varThreshold=60)

#----------------------  delta Time reader -----------------
cnt = 0
mywindow = 4   # moving average window
thres=10        
nearVal = 30

def sma(data,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(data,weights,'valid')
    # if len(sma) < mywindow:
    #     return 0
    # else: 
    return smas

serPort = serial.Serial('COM6',baudrate = 9600, timeout = 1)
deltaTimes = []

diffT = 0
curX = 0
curY = 0


#----------------------
while True:
#----------------------  delta Time reader -----------------
    cnt += 1
    period = serPort.readline().decode('ascii')
    period = period.strip()
    if len(period) > 1:
        deltaTime = int(period)
        #if(tim > 0):
        #freq = int(tim)
        # freq = int(5000/tim*1000000-10000)
        deltaTimes.append(deltaTime)
        #print(sma(x,mywindow))
        if len(deltaTimes) > mywindow+1:
            movingave = int(sma(deltaTimes,mywindow)[len(deltaTimes)-mywindow-1])
            diffT =abs(deltaTime - movingave)
            if diffT > thres:
                print(str(deltaTime) + ' ' + str(movingave) + ' ' + str(diffT) + ' !!!!!!!!' )
            else:
                print(str(deltaTime) + ' ' + str(movingave) + ' ' + str(diffT))
        else:
            print(deltaTime)
#----------------------  delta Time reader end-----------------

    check, frame = vd.read()

    #print(check)
    '''
    cur_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cur_frame = cv2.GaussianBlur(cur_frame,(21,21),0)
    if bkg_frame is None:
        bkg_frame = cur_frame
        print(cur_frame.shape)
        continue
    diff_frame = cv2.absdiff(bkg_frame, cur_frame)
    

    #print(diff_frame)
    '''
    diff_frame = subtract.apply(frame)
    
    _, diff_frame_threshold = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY) # filter out all <30 from diff_frame
    
    diff_frame_threshold = cv2.dilate(diff_frame_threshold, None, iterations=2)
    
    _,contours,_ = cv2.findContours(diff_frame_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        boxArea = cv2.contourArea(contour)
        
        if boxArea < 200 or boxArea > 10000: #pixel
            continue
        
        (x,y,w,h) = cv2.boundingRect(contour)
        
        distance = int(((abs(curX - x))**2 +  (abs(curY - y))**2)**(0.5))
        
        cv2.putText(frame, str(distance), (50, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), lineType=cv2.LINE_AA)

        if int(diffT) > int(thres):      
            if distance > nearVal:
            #if (abs(curX - x) >= nearVal and abs(curY - y) >= nearVal):
                midX = int((x+x+w)/2)
                midY = int((y+y+h)/2)
                detectBox.append([midX,midY,25])
                curX = x
                curY = y
                     
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

        areaStr = str(boxArea)
        cv2.putText(frame, areaStr, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), lineType=cv2.LINE_AA) 
    #fdeviation += 1
    #print(fdeviation)
    #print(fdeviation%500)
    
    '''
    for x1,y1,w1,h1 in detectBox:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),3) 
    '''    
      
    for x1,y1,r1 in detectBox:
        cv2.circle(frame,(x1,y1),r1,(255,0,0),3) 
    

  
    #cv2.imshow("Background",bkg_frame)
    #cv2.imshow("Current_Frame",cur_frame)
    #cv2.imshow("different_frame",diff_frame)
    #cv2.imshow("filtered_frame",diff_frame_threshold)
    cv2.imshow("frame",frame)
    cv2.resizeWindow('frame', 800,600)
    #cv2.imshow("delta",diff_frame_threshold)
    #print(diff_frame_threshold)
    
    #time.sleep(0.1)    
    key=cv2.waitKey(1)
    #print(key)
    if key == ord('q'):
        break    

vd.release()
cv2.destoryAllWindows
