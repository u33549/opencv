import cv2 as cv
import numpy as np


def clearFrame(frame):
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    frame1 = cv.bilateralFilter(frame1, 10, 35, 25)

    blank = np.zeros(frame.shape[:2], dtype='uint8')
    b, g, r = cv.split(frame1)
    frame1 = cv.merge([blank, blank, r])
    frame2 = cv.merge([blank, g, r])
    clearFrame = diff_img = cv.absdiff(frame1, frame2)
    clearFrame = (255 - clearFrame)
    clearFrame = cv.cvtColor(clearFrame, cv.COLOR_BGR2GRAY)
    threshold, clearFrame = cv.threshold(clearFrame, 175, 255, cv.THRESH_BINARY_INV)
    return clearFrame

def getContours(clearFrame,drawnFrame):
    contours, hierarchies = cv.findContours(clearFrame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    filtredContours=[]
    for c in contours:
        x = cv.contourArea(c)
        if (x > 700):
            # cv.drawContours(drawnFrame, [c], -1, (0, 255, 0), 2)
            filtredContours.append(c)
    return filtredContours,drawnFrame

