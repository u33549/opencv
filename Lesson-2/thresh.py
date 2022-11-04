import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Thresh işlemi bir yoğunluk aramasıdır 

# Resimmler grayscale olduğunda her renk (100,100,100) gibi yani (x,x,x) formatında olur 
# (x,x,x) renginin yoğunluğu x tir.
# (100,100,100) renginin yoğunluğu 100 dür.


# Resmi gri yapıp yoğunluk aramasına uygun hale getirdik
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
# cv.threshold(gray, x, y, cv.THRESH_BINARY )
# yoğunluğu xten büyük olan renklerin yoğunluğunu y olarak ayarlar
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

# Simple Thresholding -Inverted
# cv.threshold(gray, x, y, cv.THRESH_BINARY_INV )
# yoğunluğu xten küçük olan renklerin yoğunluğunu y olarak ayarlar
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
# Detaylı bilgi:https://medium.com/caglargul-blog/emgucv-ile-adaptif-e%C5%9Fikleme-adaptive-thresholding-b0a4d801aa41
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)