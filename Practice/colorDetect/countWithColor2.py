import cv2 as cv
import numpy as np

# Orijinal resim
imgPath="..\\..\\Resources\\Photos"
img = cv.imread(imgPath+'\\color.png')



hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range wanted color in HSV
lower_val = np.array([15, 50, 70])
upper_val = np.array([30, 250, 250])

# Threshold the HSV image - any green color will show up as white
mask = cv.inRange(hsv, lower_val, upper_val)

contours, hierarchies = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

counter=1



# kutu içine alma
for i in contours:
    x, y, w, h = cv.boundingRect(i)
    cv.rectangle(img, (x,y),(x+w,y+h), (0,0,255), thickness=4)
    cv.putText(img, str(counter), (x+w//2, y+h//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
    counter+=1

# cv.drawContours(img,contours,-1,(0,0,255),4)
cv.imshow('Orijinal', img)
cv.waitKey(0)