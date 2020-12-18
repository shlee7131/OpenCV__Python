'''
How to read Images, Video, WebCam
'''

import cv2
print("Package Imported")

''' 이미지 '''
img = cv2.imread("res/image.png")   #read an image

cv2.imshow("Output", img)           # show an image, 창의 이름이 Output으로 설정
cv2.waitKey(0)                       # 0 을 입력하면 무한 대기 이외는 ms 만큼 대기

''' 비디오 '''
cap = cv2.VideoCapture("res/Wildlife.mp4")      # 비디오 불러오기

while True:
    success, img = cap.read()                   # 비디오 캡쳐, success는 boolean 으로 잘 캡쳐되었는지를 확인
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       # q 가 눌러졌을때 loop 종료(동영상 실행 종료)
        break

''' 웹캠 '''

cap = cv2.VideoCapture(0)                       # 0을 입력시 웹캠 연결
cap.set(3,640)                                  # 창 크기 조정(width), id = 3
cap.set(4,480)                                  # 창 크기 조정(height), id = 4
cap.set(10, 100)                                # 밝기 조절 , id = 10

while True:
    success, img = cap.read()                   # 비디오 캡쳐, success는 boolean 으로 잘 캡쳐되었는지를 확인
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       # q 가 눌러졌을때 loop 종료(동영상 실행 종료)
        break