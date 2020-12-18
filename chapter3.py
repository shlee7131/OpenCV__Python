'''
Resizing and Cropping
'''

import cv2
import numpy as np

img = cv2.imread("res/image.png")
print(img.shape)                    # 이미지의 크기를 반환

imgResize = cv2.resize(img,(300,200))           # 300 x 200 사이즈 변경
print(imgResize.shape)

imgCropped = img[0:200, 200:500]                      # 너비와 높이 각각의 시작, 끝 인덱스로 지정

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)

