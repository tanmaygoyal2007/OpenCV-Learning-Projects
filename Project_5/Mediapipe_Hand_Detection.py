import cv2
import mediapipe as mp 

mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands=mp.solutions.hands

cap=cv2.VideoCapture(0)

p=mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5)

while cap.isOpened():
    r,frame=cap.read()
    if r== True:
        frame=cv2.resize(frame,(1000,600))
        frame=cv2.flip(frame,1)

        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        result=p.process(img)

        frame=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame,landmarks,mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Tracking",frame)
        if cv2.waitKey(25) & 0xff== ord("p"):
            break

cap.release()
cv2.destroyAllWindows()