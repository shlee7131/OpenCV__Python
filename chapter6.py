'''
Joining Image
- np.hsatck, np.vstack :수평, 수직 방향으로 붙이기
- np.hsatck, np.vstack 의 단점
    1. 이미지의 사이즈 조정 및 이미지 배치 1방향
    2. 붙이려는 이미지간의 채널의 개수가 같아야 한다
- 위의 문제를 해결하기 위해선 function을 만들어서 활용
'''
import cv2
import numpy as np

# 위의 문제들을 해결하기 위해 만들어진 Function
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


img = cv2.imread('res/image.png')
img = cv2.resize()
imgHor = np.hstack((img,img))           # 이미지를 수평 방향으로 붙이기 (Stacking)
imgVer = np.vstack((img,img))           # 이미지를 수직 방향으로 붙이기 (Stacking)


cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)
