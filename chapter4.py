'''
Shapes & Texts
'''

import cv2
import numpy as np


''' Black Canvas '''
img = np.zeros((512, 512,3))    # 0는 하나의 black pixel 을 의미한다(512x512) + channel 3 개 형성
print(img.shape)

''' Color '''
img[:] = 255,0,0                # B G R 값 => Blue
img[:] = 0,255,0                # Green
img[:] = 0,0,255                # Red

''' Line + Rectangle + Circle + Text'''
# (0,0) 에서 (300,300) 로 (0,255,255) 색의 선 그리기
cv2.line(img,(0,0),(300,300),(0,255,255))
# thickness 2
cv2.rectangle(img,(0,0),(250,350),(255,0,0),2)
# circle center (400,50), radius 30 color(0,255,0), thickness 5
cv2.circle(img,(400,50),30,(0,255,0),5)
# origin (300,100), scale 1 color (0,255,0) thickness 1
cv2.putText(img," OPENCV ", (300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

cv2.imshow("Image",img)

cv2.waitKey(0)