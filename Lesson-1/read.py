import cv2 as cv

imgPath="..\\Resources\\Photos"
videoPath="..\\Resources\\Videos"

#------------!Fotoğraf Okuma!---------------#

#imread içeriğin okunmasını sağlar ve dönüt olarak renk kodlarını döndürür
img=cv.imread(imgPath+"\\cat.jpg")
# print(img) #denemek istersen bu satırı aç

#imshow(title,img) görselin gösterilmesini sağlar
cv.imshow("Kedi",img)
#görüntü anlık olarak gidip gelmemesi için buna bekleme işlemi ya da açık kalması için şart eklememiz gerek
#waitKey(0) ile bir tuşa basılana kaar beklemesini sağlıyoruz.
cv.waitKey(0) #üstteki şartı denemek için bu satırı kapat


#------------!Video Okuma!---------------#
#Temelde fotoğraf okuma ile benzer bir çalışması var

#VideoCapture videonun okunmasını sağlar eğerki dosya yolu yerine 0 değerini girerseniz kameranıza bağlanır.

capture=cv.VideoCapture(videoPath+"\\kitten.mp4")
# print(capture) #yazdırman sana hiç bir şey kazandırmayacak ama denemek istersen

#resimin aksine videoyu sahne sahne incelioruz bu sebeple döngü kullanmamız gerekor.
while True:
    isTrue, frame=capture.read() #burda hem frame hem de isTrue isimli iki değişkene anlık gelen sahneyi atadık eğerki sahne boşsa yani video bitmişse döngüden çıkılması için
    #print(frame) #.read kullandığımızda fotoğrafın renk kodlarına ulaştığımızı artık fark etmişsindir ama eğer edemediysen çalıştır
    if isTrue:
        cv.imshow('kedi2', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):#herhangi bir tuşa basıldığında videoyu kapatmak için
            break
    else:
        break

capture.release() #sistemi zorlamaması amacıyla video ya da kamerayı kapatır
cv.destroyAllWindows() #açılan tüm pencereleri kapatır
