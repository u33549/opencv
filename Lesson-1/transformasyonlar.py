import cv2 as cv
import numpy as np

imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\park.jpg')


# Taşıma
def translate(img, x, y): #taşıma için bir fonksyon mantığını yazmaya üşendim
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    print(transMat)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> sol
# -y --> yukarı
# x --> sağ
# y --> aşağı

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)
cv.destroyAllWindows()

# Döndürme
def rotate(img, angle, rotPoint=None):#Döndürme için bir fonksyon mantığını yazmaya üşendim
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
cv.waitKey(0)
cv.destroyAllWindows()


rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', rotated_rotated)
cv.waitKey(0)
cv.destroyAllWindows()


# Takla
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)
cv.waitKey(0)
cv.destroyAllWindows()

# Kırpma
cropped = img[50:300, 50:400] #Pythonda kullanılan diziden parça alma işlemidir
cv.imshow('Cropped', cropped)
cv.waitKey(0)
cv.destroyAllWindows()

cv.waitKey(0)