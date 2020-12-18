''' Color Detection'''

import cv2
import numpy as np

def empty():
    pass

path = "res/image.png"

'''
<초기값>
Hue : 0 ~ 179
Sat : 0 ~ 255
Val : 0 ~ 255

<Mask 생성 후>
해당 색 영역 검출을 위한 값 확인 후 재설정
'''
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("Hue Min","TrackBars",6,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",88,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",223,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

''' 
<HSV 색공간>

H(Hue): 색조
S(Saturation): 채도
V(Value): 명도
- RGB와 같이 색들의 조합이 아닌 색깔 그 자체를 알려주므로 직관성이 좋다.
- 색 검출에 효율적이다
- H:0 Red <-> H:120 Green <-> H:240 Blue <-> H:360 Red
'''

''' Detecting Green '''
while True:
    # 실시간 HSV 트래킹을 위해 무한 루프 형성
    img = cv2.imread(path)
    img = cv2.resize(img,(300,300))


    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)                # convert BGR -> HSV
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)                  # 검출 색 범위 지정

    imgResult = cv2.bitwise_and(img,img,mask=mask)          # add two images together as one image

    cv2.imshow("Original", img)
    cv2.imshow("BGR to HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)                                          # 1ms