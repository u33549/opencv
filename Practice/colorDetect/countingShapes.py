import cv2 as cv
import numpy as np

# Orijinal resim
imgPath="..\\..\\Resources\\Photos"
img = cv.imread(imgPath+'\\color.png')
# cv.imshow('Orijinal', img)
# cv.waitKey(0)
# cv.destroyAllWindows()



# keskin kenarların belirlenmesi
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY_INV )
cv.imshow("tresh",thresh)

# Kontürlerin çizilmesi
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
counter=1

# kutu içine alma
for i in contours:
    x, y, w, h = cv.boundingRect(i)
    cv.rectangle(img, (x,y),(x+w,y+h), (25,50,100), thickness=4)
    cv.putText(img, str(counter), (x+w//2, y+h//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,50,25), 2)
    counter+=1

cv.drawContours(img,contours,-1,(100,100,100),4)
cv.imshow('Orijinal', img)
cv.waitKey(0)