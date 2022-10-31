import cv2 as cv
import numpy as np

videoPath="..\\..\\Resources\\Videos"
capture=cv.VideoCapture(videoPath+"\\drone1.mp4")

while True:
    isTrue, frame=capture.read()
    if isTrue:
        frame1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        frame1= cv.bilateralFilter(frame1, 10, 35, 25)

        blank = np.zeros(frame.shape[:2], dtype='uint8')
        b, g, r = cv.split(frame1)
        frame1 = cv.merge([blank, blank, r])
        frame2 = cv.merge([blank, g, r])
        # frame3 = cv.merge([b, blank, r])
        a=diff_img = cv.absdiff(frame1, frame2)
        # a=diff_img = cv.absdiff(a, frame3)

        a = (255-a)
        a = cv.cvtColor(a, cv.COLOR_BGR2GRAY)

        threshold, a = cv.threshold(a, 175, 255, cv.THRESH_BINARY_INV)
        # a = cv.Canny(a, 120, 125)
        # cv.imshow('a1', a)
        # cv.imshow('a2', frame3)
        # cv.imshow('a3', frame2)

        cv.imshow('a1', a)
        contours, hierarchies = cv.findContours(a, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        for c in contours:
            x=cv.contourArea(c)
            if(x>500):
                cv.drawContours(frame, [c], -1, (0, 255, 0), 3)

        cv.imshow('a', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()