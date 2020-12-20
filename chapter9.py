''' Face Detection '''
''' 
- Haar Cascade xml 파일을 통해 검출한다
- Positive Faces / Negative Faces 정보 -> 다단계 기계 학습
'''
import cv2


faceCascade = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")
img = cv2.imread('res/sejong.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

print(img[10,10],imgRGB[10,10])
cv2.imshow('Result',img)
cv2.waitKey(0)