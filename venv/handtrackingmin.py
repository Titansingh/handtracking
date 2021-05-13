import cv2
import mediapipe as mp
import time
import  socketio

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
ptime = 0
ctime = 0

while True:


    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
                   mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    ctime = time.time()
    fps  =1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),3)
    cv2.imshow("Image2", img)
    cv2.waitKey(1)