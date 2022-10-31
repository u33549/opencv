import cv2 as cv

imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\park.jpg')

cv.imshow('Park', img)
cv.waitKey(0)
cv.destroyAllWindows()



# Gri tonlamalı hale getir
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()



# Bulanıklık
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)
cv.destroyAllWindows()



# Kenar Belirleme
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)
cv.destroyAllWindows()


# Yayma/Genişletme
dilated = cv.dilate(img, (7,7), iterations=10)
cv.imshow('Dilated', dilated)
cv.waitKey(0)
cv.destroyAllWindows()



# Aşındırma
eroded = cv.erode(img, (7,7), iterations=20)
cv.imshow('Eroded', eroded)
cv.waitKey(0)
cv.destroyAllWindows()

