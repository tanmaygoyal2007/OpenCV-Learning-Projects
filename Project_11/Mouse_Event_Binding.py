import cv2
import numpy as np

def python(event,x,y,f,p):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),4)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+20,y+20),(0,255,0),4)
cv2.namedWindow("Mouse")

img=np.ones((600,600,3),np.uint8)*255
cv2.setMouseCallback("Mouse",python)
while True:
    cv2.imshow("Mouse",img)
    if cv2.waitKey(25) & 0xff == ord("p"):
        break
cv2.destroyAllWindows()

