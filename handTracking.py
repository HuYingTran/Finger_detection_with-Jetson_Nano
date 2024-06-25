import cv2
import mediapipe as mp

#Cau hinh va khia bao doi tuong
mp_drawing_util = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(
    model_complexity = 0,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

#Mo may anh
cap = cv2.VideoCapture("test.mp4")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    alphabet = ''

    if result.multi_hand_landmarks:
        myHand = []
        for idx, hand in enumerate(result.multi_hand_landmarks):
            #ve toa do khung xuong
            mp_drawing_util.draw_landmarks(img, hand, mp_hand.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                #lay cac toa do
                h,w, _ = img.shape
                myHand.append([int(lm.x*w),int(lm.y*h)])
    
    cv2.imshow("nhan dang",img)
    key=cv2.waitKey(1)
    if key ==27:
        break
cap.release()
