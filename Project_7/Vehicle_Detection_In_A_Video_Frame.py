import cv2
cap=cv2.VideoCapture("videos/cars.mp4")

while True:
    r,frame=cap.read()
    if r == True:
        gry=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        car=cv2.CascadeClassifier("cars.xml")

        cars=car.detectMultiScale(gry,1.2,3)
        
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

        cv2.imshow("Detection",frame)
        if cv2.waitKey(25) & 0xff == ord("p"):
            break

cap.release()
cv2.destroyAllWindows()