import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow("con")
cv2.createTrackbar("th","con",0,255,nothing)

cv2.createTrackbar("lb","con",0,255,nothing)
cv2.createTrackbar("lg","con",0,255,nothing)
cv2.createTrackbar("lr","con",0,255,nothing)

cv2.createTrackbar("hb","con",255,255,nothing)
cv2.createTrackbar("hg","con",255,255,nothing)
cv2.createTrackbar("hr","con",255,255,nothing)

cap=cv2.VideoCapture(0)
while cap.isOpened():
    r,frame=cap.read()
    if r == True:
        thr=cv2.getTrackbarPos("th","con")

        LB=cv2.getTrackbarPos("lb","con")
        LG=cv2.getTrackbarPos("lg","con")
        LR=cv2.getTrackbarPos("lr","con")

        HB=cv2.getTrackbarPos("hb","con")
        HG=cv2.getTrackbarPos("hg","con")
        HR=cv2.getTrackbarPos("hr","con")

        lower=np.array([LB,LG,LR])

        upper=np.array([HB,HG,HR])

        frame=cv2.flip(frame,1)
        frame=cv2.resize(frame,(300,300))
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        m=cv2.inRange(hsv,lower,upper)
        res=cv2.bitwise_and(frame,frame,mask = m)
        fr=cv2.bitwise_not(res)


        _,thi=cv2.threshold(m,thr,255,cv2.THRESH_BINARY)
        cnt,hr=cv2.findContours(thi,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame,cnt,-1,(255,0,0),2)

        cv2.imshow("thr",thi)
        cv2.imshow("mask",m)
        cv2.imshow("res",res)
        cv2.imshow("org",frame)
        if cv2.waitKey(25) & 0xff == ord("p"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()