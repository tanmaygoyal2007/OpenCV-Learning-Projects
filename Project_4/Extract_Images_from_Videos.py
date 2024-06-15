import cv2
cap=cv2.VideoCapture("videos/swim.mp4")
c=0
while True:
    r,frame=cap.read()
    if r == True:
        filename="images/org_img_"+str(c)+".jpg"
        cv2.imwrite(filename,frame)
        cv2.imshow("video",frame)
        c=c+1
        if cv2.waitKey(25) & 0xff == ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()