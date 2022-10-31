import cv2 as cv
import numpy as np

imgPath="..\\Resources\\Photos"

# orijinal resim okundu
img=cv.imread(imgPath+"\\cat.jpg")
cv.imshow('Cats', img)
cv.waitKey(0)
cv.destroyAllWindows()

# kontürlerin aktarılması için tuval oluşturuldu
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.waitKey(0)
cv.destroyAllWindows()

# Resim gri tonlamalı hale getirildi
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()

# resim bulanıklaştırıldı
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)
cv.destroyAllWindows()

# resimdeki kenarlar bulundu
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)
cv.destroyAllWindows()

# kontürler bulundu
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #parametreler ile ilgili detaylı bilgi https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
print(f'{len(contours)} contour(s) found!')


# kontürler tuvale aktarıldı
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()