import cv2
import numpy  as np

img=cv2.imread("photos/img17.png")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edg=cv2.Canny(gry,20,250)

l=cv2.HoughLinesP(edg,1,np.pi/180,200,minLineLength = 180,maxLineGap=100)

for i in l:
    x1,y1,x2,y2=i[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyWindow()