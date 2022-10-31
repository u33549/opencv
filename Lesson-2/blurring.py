import cv2 as cv

imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\cats.jpg')
cv.imshow('Cats', img)

# Average Blur
average = cv.blur(img, (7,7))
# Her pikseli x genişliğe ve y yüksekliğe sahip bir dörtgenin merkezi olarak atar ve çevresindeki pikselin ortalaması şeklinde değerlendirerek bulanıklık sağlar
# cv.blur(sahne, (x,y))
cv.imshow('Average Blur', average)
cv.waitKey(0)
cv.destroyAllWindows()


# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
# Temelde ortalama methodu ile aynı çalışır ama farklı olarak her piksellerin belli bir ağırlığı vardır ve bunuda hesaba katar
# cv.GaussianBlur(sahne, (x,y),ağırlık)
cv.imshow('Gaussian Blur', gauss)
cv.imshow('Cats', img)
cv.waitKey(0)
cv.destroyAllWindows()


# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
cv.imshow('Cats', img)
cv.waitKey(0)
cv.destroyAllWindows()
# Her pikseli x genişliğe karenin merkezi olarak atar ve çevresindeki piksellerin medyanı şeklinde değerlendirerek bulanıklık sağlar
# cv.GaussianBlur(sahne,x )

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# Ayrıntılı bilgi https://en.wikipedia.org/wiki/Bilateral_filter
# Ayrıntılı olarak çalışmamantığından bahsedemeyeceğim ama bu bulanıklaştırma işlemi keskin kenarları korur
cv.imshow('Bilateral', bilateral)
cv.imshow('Cats', img)
cv.waitKey(0)
cv.destroyAllWindows()

