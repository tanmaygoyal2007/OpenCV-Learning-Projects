import cv2
cap=cv2.VideoCapture("videos/jog.mp4")

while True:
    r,frame=cap.read()
    if r == True:
        gry=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        hm=cv2.CascadeClassifier(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_fullbody.xml")
        h=hm.detectMultiScale(gry,1.2,3)

        for x,y,w,h in h:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

        cv2.imshow("Detection",frame)
        if cv2.waitKey(25) & 0xff == ord("p"):
            break

cap.release()
cv2.destroyAllWindows()