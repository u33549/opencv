import cv2 as cv
import numpy as np

# Orijinal resim
imgPath="..\\..\\Resources\\Photos"
img = cv.imread(imgPath+'\\color.png')
blank = np.zeros(img.shape[:2], dtype='uint8')
imgC=img.copy()
imgC[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]

# cv.imshow('Orijinal', img)
# cv.waitKey(0)
# cv.destroyAllWindows()



# keskin kenarların belirlenmesi

b,g,r = cv.split(imgC)
print(b,g,r)
blue = cv.merge([blank,g,r])
# cv.imshow("notb",blue)

b,g,r = cv.split(blue)
green = cv.merge([blank,g,blank])
green[np.where((green==[0,255,0]).all(axis=2))] = [255,255,255]

# cv.imshow("g",green)

red = cv.merge([blank,blank,r])
red[np.where((red==[0,0,255]).all(axis=2))] = [255,255,255]
# cv.imshow("r",red)

bitwise_or = cv.bitwise_or(green,red)
# cv.imshow('Bitwise AND', bitwise_and)

threshold, thresh = cv.threshold(bitwise_or, 230, 255, cv.THRESH_BINARY_INV )
cv.imshow("thresh",thresh)
gray = cv.cvtColor(thresh, cv.COLOR_BGR2GRAY)

# Kontürlerin çizilmesi
contours, hierarchies = cv.findContours(gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
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