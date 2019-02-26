import cv2, time

# img = cv2.imread(r'C:\Users\jay\Pictures\Capture.PNG')
# print(type(img))
# print(img)
# print(img.shape)

fdeviation = 0
fthreshold = 50

print("Starting object detection...")
time.sleep(2)

vd = cv2.VideoCapture(0)  #0 denote first camera. if video file, input path

print("Webcam opened.")
print("First frame capture in 3 seconds.")

# _, frame0 = vd.read()
# frame0gray = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
# frame = cv2.GaussianBlur(gray0,(21,21),0)

detectBox =[]

bkg_frame = None

while True:
    check, frame = vd.read()
    print(check)
    
    cur_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cur_frame = cv2.GaussianBlur(cur_frame,(21,21),0)

    if bkg_frame is None:
        bkg_frame = cur_frame
        continue

    diff_frame = cv2.absdiff(bkg_frame, cur_frame)
    

    #print(diff_frame)
    
    _, diff_frame_threshold = cv2.threshold(diff_frame, 100, 255, cv2.THRESH_BINARY) # filter out all <30 from diff_frame
    
    diff_frame_threshold = cv2.dilate(diff_frame_threshold, None, iterations=2)
    
    _,contours,_ = cv2.findContours(diff_frame_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000: #pixel
            continue
        
        (x,y,w,h) = cv2.boundingRect(contour)
    
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    fdeviation += 1
    print(fdeviation)
    print(fdeviation%500)
    
    if fdeviation%50 == 0:
        detectBox.append([x,y,w,h])        
        
        print(fdeviation%500)
    
    for x1,y1,w1,h1 in detectBox:
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),3)


    #cv2.imshow("Background",bkg_frame)
    #cv2.imshow("Current_Frame",cur_frame)
    #cv2.imshow("different_frame",diff_frame)
    #cv2.imshow("filtered_frame",diff_frame_threshold)
    cv2.imshow("frame",frame)

    #print(diff_frame_threshold)
    
    time.sleep(0.1)    
    key=cv2.waitKey(1)
    print(key)
    if key == ord('q'):
        break    

vd.release()
cv2.destoryAllWindows