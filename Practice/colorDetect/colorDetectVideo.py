import cv2 as cv
import numpy as np

videoPath="..\\..\\Resources\\Videos"
capture=cv.VideoCapture(videoPath+"\\color1.mp4")


def upLow(r,g,b):
    color = np.uint8([[[b, g, r]]])  # here insert the bgr values which you want to convert to hsv
    hsvColor = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    lowerLimit = hsvColor[0][0][0] - 10, 100, 100
    upperLimit = hsvColor[0][0][0] + 10, 255, 255
    return lowerLimit,upperLimit



while True:
    isTrue, frame=capture.read()
    if isTrue:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range wanted color in HSV
        lower_val = np.array(upLow(0,0,255)[0])
        upper_val = np.array(upLow(0,0,255)[1])

        mask = cv.inRange(hsv, lower_val, upper_val)
        contours, hierarchies = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        for i in contours:
            x, y, w, h = cv.boundingRect(i)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=4)

        cv.imshow('a', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()