'''
Contours(폐곡선) / Shape Detection
'''

import cv2
import numpy as np

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

def getContours(img):
    # Outer Line Detect, findContours = 이미지에서 contour를 찾은 후 리스트형 자료에 담아 리턴
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)     # 해당 폐곡선의 면적
        #print(cnt)                      # Contour 영역
        if area >  500:
            cv2.drawContours(imgContour, cnt, contourIdx=-1, color=(255, 0, 0), thickness=3)  # draw contours
            peri = cv2.arcLength(cnt, True) # 선 길이 구하기 , True -> It is Closed Line !
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) #  꼭지점 구하기 , True -> It is Closed Line !
            print(len(approx))
            objCor = len(approx)
            ''' 객체에 Bounding Box 만들기'''
            x,y,w,h = cv2.boundingRect(approx) # x, y 좌표 + 너비, 높이

            if objCor == 3: objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: # 오차범위 5%
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            else: objectType = "None"

            cv2.rectangle(imgContour, (x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                        (0,0,0),2)

path = "res/shape.png"
img = cv2.imread(path)
imgContour = img.copy()

''' gray scale -> edge detection'''
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))


cv2.imshow("Stack",imgStack)



cv2.waitKey(0)