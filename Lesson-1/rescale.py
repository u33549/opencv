import cv2 as cv

imgPath="..\\Resources\\Photos"
videoPath="..\\Resources\\Videos"




#------------!Çerçeve Boyutlama!---------------
def rescaleFrame(frame, scale): #sahnemizi boyutlandırmak için bir fonksyon tanımladık ve 2 değişken alıyor sahne ve boyut
    width = int(frame.shape[1] * scale) #shape[1] sahnenin enini döndürürken
    height = int(frame.shape[0] * scale) #shape[0] sahnenin yükesliğini döndürür
    #isterseniz 0 ve 1 in yerini değiştirip olacakları deneyin
    dimensions = (width,height) #ebatlarımızı bir değişkene atadık
    return cv.resize(frame, dimensions) #ardından ebatlarımızı sahnenin üstünde uygulayıp geri döndürdük


#fotoğraf örneği
img=cv.imread(imgPath+"\\cat.jpg")
cv.imshow("Kedi boyutlandirildi",rescaleFrame(img,0.50))
cv.imshow("Kedi orijinal",img)

cv.waitKey(0)


#video örneği
capture=cv.VideoCapture(videoPath+"\\kitten.mp4")
while True:
    isTrue, frame=capture.read()
    if isTrue:
        cv.imshow('kedi2 boyutlandirildi', rescaleFrame(frame,0.50))
        cv.imshow('kedi2 orijinal', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()