from collections import  deque
import numpy as np
import xyz_calculate
#import imutils
import cv2
import time
def truncate(self, n, decimals=0):
    n = float(n)
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#Set the red threshold in rad space
redLower = np.array([170, 100, 100])
redUpper = np.array([179, 255, 255])
#Initializes the trace list
mybuffer = 64
pts = deque(maxlen=mybuffer)
#open camera（you need two camera connected first）
video1="http://admin:admin@192.168.137.13:8081/"
video2="http://admin:admin@192.168.137.21:8081/"

camera1 = cv2.VideoCapture(video1)
camera2=cv2.VideoCapture(video2)
#wait for a minute
time.sleep(1)
# Go through each frame and check the red cap
while True:
    #read a frame in one loop
    (ret, frame) = camera1.read()
    (ret2,frame2)=camera2.read()
    #judge if both camera are opened,if so, go on
    if not ret and ret2:
        print ('No Camera')
        break
    #frame = imutils.resize(frame, width=600)
    #transform the picture from rgb space to hsv space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hsv2=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)

    #The mask is constructed according to the threshold value
    mask = cv2.inRange(hsv, redLower, redUpper)
    #Corrosion operation
    mask2=cv2.inRange(hsv2,redLower,redUpper)
    mask = cv2.erode(mask, None, iterations=2)

    mask2=cv2.erode(mask2,None,iterations=2)
    #The purpose of the expansion operation is to remove the noise
    mask = cv2.dilate(mask, None, iterations=2)

    mask2=cv2.dilate(mask2,None,iterations=2)
    #contour detection
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    cnts2=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    #Initializes the center of mass of the cap circle
    center = None
    #If there is an outline
    if len(cnts) and len(cnts)==len(cnts2) :
        #Find the contour with the largest area
        c = max(cnts, key = cv2.contourArea)
        c2=max(cnts2, key = cv2.contourArea)
        #Determine the circumferential circle of the contour with the largest area
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        ((x2,y2),radius2)=cv2.minEnclosingCircle(c2)
        #Calculate the moment of the contour
        M = cv2.moments(c)
        M2=cv2.moments(c2)
        #Calculate the center of mass
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
        center2= (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
        #The drawing is performed only if the radius is greater than 10
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            xw,yw,zw=xyz_calculate.calculate_world_xyz(x,y,x2,y2)
            cv2.putText(frame, "X,Y,Z: "+str(int(xw))+","+str(int(yw))+","+str(int(zw))+"!",(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            #Add the center of mass to the PTS, and to the left of the list
            pts.appendleft(center)
    #Traverse the tracking points and plot the tracks in sections
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        #Calculate the thickness of the small line segment
        thickness = int(np.sqrt(mybuffer / float(i + 1)) * 2.5)
        #draw a little line segment
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    #res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Frame', frame)
    #Keyboard detection, esc key exit detected
    k = cv2.waitKey(5)&0xFF
    if k == 27:
        break
#release camera process
camera1.release()
#close all the windows
cv2.destroyAllWindows()
