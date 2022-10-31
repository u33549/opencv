import cv2 as cv
import numpy as np

# Orijinal resim
imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\cats 2.jpg')
cv.imshow('Cats', img)
cv.waitKey(0)
cv.destroyAllWindows()


# Maskeleme için fare figürü
blank = np.zeros(img.shape[:2], dtype='uint8')
w=img.shape[1]//2-200
h=img.shape[0]//2-50
r=75
circle1 = cv.circle(blank.copy(), (w + r,h), r, 255, -1)
circle2 = cv.circle(blank.copy(), (w + 3*r,h), r, 255, -1)
circle3 = cv.circle(blank.copy(), (w + 70,h-10), 20, 255, -1)
circle4 = cv.circle(blank.copy(), (w +4*r-70,h-15), 20, 255, -1)
pts = np.array([[w,h],[w+2*r,h+2*r],[w+4*r,h]], np.int32)
a=cv.drawContours(blank.copy(),[pts],-1,(255,255,255),thickness=cv.FILLED)
c1 = cv.bitwise_or(circle1,circle2)
mause =cv.bitwise_or(c1,a)
mause = cv.bitwise_xor(mause,circle3)
mause = cv.bitwise_xor(mause,circle4)
cv.imshow('Mause', mause)
cv.waitKey(0)
cv.destroyAllWindows()


# Maskeleme işlemi bir fotoğrafın belli bir kısmının gösterilip diğer kısmın ayrılması olarak tanımlanabilir
# Kare bir maske oluşturursak sadece karenin ardı gözükür
masked = cv.bitwise_and(img,img,mask=mause)
cv.imshow('Weird Shaped Masked Image', masked)
cv.waitKey(0)
cv.destroyAllWindows()
