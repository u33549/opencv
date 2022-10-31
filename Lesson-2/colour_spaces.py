import cv2 as cv

imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\park.jpg')
cv.imshow('Park', img)
cv.waitKey(0)
cv.destroyAllWindows()



# Gri Tonlamalı Yapma
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()



# HSV Renk Uzayına Çevirme
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
cv.waitKey(0)
cv.destroyAllWindows()



# LAB Renk Uzayına Çevirme
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
cv.waitKey(0)
cv.destroyAllWindows()



# Renkleri Tersine Çevirme
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
cv.waitKey(0)
cv.destroyAllWindows()


