'''
Warp Perspective - 기하학적 변환
'''

import cv2
import numpy as np

img = cv2.imread("res/image.png")                               # get it as flat

width,height = 250, 350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])    # 이미지의 꼭짓점 4개 매핑 ( 좌 상단 , 우 상단, 우 하단, 좌 하단)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])  # 새롭게 만들 이미지 크기
matrix = cv2.getPerspectiveTransform(pts1, pts2)                # 꼭지점 기반 해당하는 정보 대응
imgOutput = cv2.warpPerspective(img, matrix, (width,height))



cv2.imshow("Image",img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)