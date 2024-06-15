import cv2
img=cv2.imread("photos/img24.webp")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

f=cv2.CascadeClassifier(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
d=f.detectMultiScale(gry,1.3,2)

for (x,y,w,h) in d:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


