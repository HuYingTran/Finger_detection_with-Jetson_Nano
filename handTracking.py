import cv2
import mediapipe as mp
import math

#Cau hinh va khia bao doi tuong
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Khai bao mang 2 chieu
points = []
led = [0,0,0,0,0]

#ham tinh khoang cach ngon tay
def distance_points(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#Mo may anh
cap = cv2.VideoCapture("test.mp4")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #lay cac toa do
                h,w,c = img.shape
                cx, cy, = int(lm.x*w), int(lm.y*h)
                points.append((cx,cy))
                if id == 0:
                    cv2.circle(img, (cx,cy), 25, (255,0,255), cv2.FILLED)
                else:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    #xu ly ngon tay
    mau = 100#distance_points(points[5],points[9])
    
    #if distance_points(points[4],points[1])< mau:
    led[0]= distance_points(points[4],points[1])< mau
    #if distance_points(points[8],points[5])< mau:
    led[1]=distance_points(points[8],points[5])< mau
    #if distance_points(points[12],points[9])< mau:
    led[2]=distance_points(points[12],points[9])< mau
    #if distance_points(points[16],points[13])< mau:
    led[3]=distance_points(points[16],points[13])< mau
    #if distance_points(points[20],points[17])< mau:
    led[4]=distance_points(points[20],points[17])< mau

    points.clear() # clear mang
    for id in range(len(led)):
    	if led[id] == 1:
    	    cv2.circle(img, (20+100*id,20), 30, (200,200,200), cv2.FILLED)
    	else:
    	    cv2.circle(img, (20+100*id,20), 30, (0,255,0), cv2.FILLED)
    
    cv2.imshow("nhan dang",img)
    key=cv2.waitKey(1)
    if key ==27:
        break
cap.release()

