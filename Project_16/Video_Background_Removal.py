import cv2
cap=cv2.VideoCapture("videos/jog.mp4")

alg01=cv2.createBackgroundSubtractorKNN(detectShadows=True)
alg02=cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while True:
    r,frame=cap.read()
    if r == True:
        frame=cv2.resize(frame,(500,400))
        r1=alg01.apply(frame)
        r2=alg02.apply(frame)
        cv2.imshow("original",frame)
        cv2.imshow("alg01",r1)
        cv2.imshow("alg02",r2)
        if cv2.waitKey(25) & 0xff == ord ("p"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()