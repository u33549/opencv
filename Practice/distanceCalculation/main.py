import cv2 as cv
import numpy as np

import calculations as calc
import filters

videoPath="..\\..\\Resources\\Videos"
capture=cv.VideoCapture(videoPath+"\\drone1.mp4")






while True:
    isTrue, frame=capture.read()
    if isTrue:
        clearFrame=filters.clearFrame(frame)
        contours,drawnFrame=filters.getContours(clearFrame,frame)
        try:
            m=calc.getSlope(contours,frame)
            calc.findCenterOfGravity(contours,frame)
        except Exception as e:
            print(e)
            pass
        cv.imshow('DetectedPos', drawnFrame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()