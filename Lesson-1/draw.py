import cv2 as cv
import numpy as np
# hatırlayacağın üzere okuma işleminde aslında sahnenin renk kodlarını okuyorduk
# yani kendi oluşturacağımız bir renk kodu dizesinide okuyabiliriz

blank = np.zeros((500,500,3)) #eğerki numpy ve rgb mantığını bilmiyorsan açıklıyım





#rgb(red green blue) yani vermiş olduğum değerler içindeki bulunma miktarını belirler min0 max 255 değerini alır
# örnek bazı renkler
# siyah =>(0,0,0)
# beyaz =>(255,255,255)
# kırmızı =>(255,0,0)
# yeşil =>(0,255,0)
# mavi =>(0,0,255)
# mor =>(255,0,255)
# sarı =>(0,255,255)

# !ancak opencv okuma sırasında bgr sırası ile okumaktadır yani mavi elde etmek için (0,0,255) değil (255,0,0) kullanmanız gerekir

#numpy olayıne gelirsek numpy bir veri,dizi,matris vb vb işleme kütüphanesidir
#kullanmış olduğumuz np.zeros((500,500,3) ifadesi ise yüksekliği ve genişliği 500 olan ve her ögesi 3 ögeden oluşan ve tüm ögelerin değerlerinin 0 olduğu bir matris döndürür
#yani
# [[0 0 0] [0 0 0] [0 0 0] [0 0 0] ... 500tane]
# [[0 0 0] [0 0 0] [0 0 0] [0 0 0] ... 500tane]
# [[0 0 0] [0 0 0] [0 0 0] [0 0 0] ... 500tane]
# [[0 0 0] [0 0 0] [0 0 0] [0 0 0] ... 500tane]
#           ...500 tane



cv.imshow('Blank', blank) #tamamı siyah bir alan gösterildi
cv.waitKey(0)
cv.destroyAllWindows()

# 1. Belli bir alanı boyamak
blank[200:300, 200:300] = 0,0,255 #bu işlem dizenin belli kızımlarındaki renk kodlarını değiştirip bir daha gösterterek kullanır
cv.imshow('Red', blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank = np.zeros((500,500,3)) #alanı sıfırlamak için

# 2. Bir dikdörtgen çizmek
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# rectangle(değiştirilcek sahne/renk matrisi, orijinin sahne köşesine göre kordinatları, boyutlar, renk kodu, thickness=kalınlık değeri)
#thickness=-1 içi dolu yani solid bir obje çizmeyi sağlamakta
cv.imshow('Dikdortgen', blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank = np.zeros((500,500,3)) #alanı sıfırlamak için

# 3. Bir çember çizmek
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-1)
# circle(değiştirilcek sahne/renk matrisi, orijinin sahne köşesine göre kordinatları, çemberin yarı çapı, renk kodu, thickness=kalınlık değeri)
#thickness=-1 içi dolu yani solid bir obje çizmeyi sağlamakta
cv.imshow('Circle', blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank = np.zeros((500,500,3)) #alanı sıfırlamak için


# 4. Çizgi çekme
cv.line(blank, (100,100), (250,250), (255,255,255), thickness=3)
cv.line(blank, (100,400), (250,250), (255,255,255), thickness=3)
cv.line(blank, (400,100), (250,250), (255,255,255), thickness=3)
cv.line(blank, (400,400), (250,250), (255,255,255), thickness=3)
# line(değiştirilcek sahne/renk matrisi, başlangıç noktası kordinatları, bitiş noktası kordinatları, renk kodu, thickness=kalınlık)
cv.imshow('Line', blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank = np.zeros((500,500,3)) #alanı sıfırlamak için

# 5. Yazı Yazma
cv.putText(blank, 'KARPUZ MELIH!!!', (105,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 1)
# putText(değiştirilcek sahne/renk matrisi, metin , başlangıç noktası kordinatları, font tipi, font büyüklüğü, renk kodu, kenarlık kalınlığı)

cv.imshow('Text', blank)
cv.waitKey(0)
cv.destroyAllWindows()
blank = np.zeros((500,500,3)) #alanı sıfırlamak için

