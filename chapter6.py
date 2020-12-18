'''
Joining Image
- np.hsatck, np.vstack :수평, 수직 방향으로 붙이기
- np.hsatck, np.vstack 의 단점
    1. 이미지의 사이즈를 조정할 수 없다
    2. 붙이려는 이미지간의 채널의 개수가 같아야 한다
- 위의 문제를 해결하기 위해선 function을 만들어서 활용
'''
import cv2
import numpy as np

img = cv2.imread('res/image.png')

imgHor = np.hstack((img,img))           # 이미지를 수평 방향으로 붙이기 (Stacking)
imgVer = np.vstack((img,img))           # 이미지를 수직 방향으로 붙이기 (Stacking)


cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)
