'''
Basic Functions
- gray
- blur
- canny
- dilation
- erosion
'''

import cv2
import numpy as np

img = cv2.imread("res/image.png")
kernel = np.ones((5,5), np.uint8)     # 5 x 5 사이즈 커널(픽셀 선택 이동 창)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # RGB -> Gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)         # Blur 정도 입력
imgCanny = cv2.Canny(img,100,100)                   # 이미지의 Edge 추출. + threshold 밸류(임계값) 추가
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)         # 이미지(테두리) 두껍게 만들기, iterations 비례
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)     # 이미지(테두리) 얇게 만들기, iterations 비례

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)


