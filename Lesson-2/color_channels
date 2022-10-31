import cv2 as cv
import numpy as np

imgPath="..\\Resources\\Photos"
img = cv.imread(imgPath+'\\park.jpg')


# Bu kısımda resimin renk kanallarını ayıracağız temelde resim 4 kanldan oluşur
# Kırmızı kanal
# Yeşil kanal
# Mavi kanal
# Gri kanal
# Gri kanalın temel kullanımı renk yoğunluğu ve koyuluk analizi olduğundan burda değinmeyeceğiz

# Belli bir kanalı almak demek sadece o rengin bulunduğu pixelleri seçmek demektir mesela kırmızı kanalı seçersek içinde kırmızı bulundurmayan renkler gözükmez
# sarı,mavi,yeşil vb..
# aynı zamanda ara renklerin kırmızı harici kısımları gözükmez mesela mor sadece kırmızı değeri gözükür.

blank = np.zeros(img.shape[:2], dtype='uint8') #açtığımız resimle aynı boyutlarda bir sahne oluşturduk

b,g,r = cv.split(img) #açtığımız resmin bgr(mavi,yeşil,kırmızı) değerlerini farklı değişkenlere atadık

blue = cv.merge([b,blank,blank])
#mavi kanal açmak için mavi değeri yazdırıp kalan kısmı bizim oluşturduğumuz boş sahneyi koyduk.
# alttada aynı işlem farklı renkler için tekrarlanmıştır.
cv.imshow('Blue', blue)
cv.waitKey(0)
cv.destroyAllWindows()

# Yeşil
green = cv.merge([blank,g,blank])
cv.imshow('Green', green)
cv.waitKey(0)
cv.destroyAllWindows()

# Kırmızı
red = cv.merge([blank,blank,r])
cv.imshow('Red', red)
cv.waitKey(0)
cv.destroyAllWindows()

# Mor
purple = cv.merge([b,blank,r])
cv.imshow('Purple', purple)
cv.waitKey(0)
cv.destroyAllWindows()

# Sarı
yellow = cv.merge([b,g,blank])
cv.imshow('Yellow', yellow)
cv.waitKey(0)
cv.destroyAllWindows()

#Kahverengi
brown = cv.merge([blank,g,r])
cv.imshow('Brown', brown)
cv.waitKey(0)
cv.destroyAllWindows()


merged = cv.merge([b,g,r]) #tüm renklerin birleştirilmiş hali yani orijinal resim
cv.imshow('Merged Image', merged)
cv.waitKey(0)
cv.destroyAllWindows()
