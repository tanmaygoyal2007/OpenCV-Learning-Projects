import cv2
img=cv2.imread("photos/img23.jpg")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sm=cv2.CascadeClassifier(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_smile.xml")
fc=cv2.CascadeClassifier(r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

f=fc.detectMultiScale(gry,1.3,3)

for x,y,w,h in f:
    roi_gry=gry[y:y+h,x:x+w]
    roi_img=img[y:y+h,x:x+w]
    
    s=sm.detectMultiScale(roi_img,1.8,7)

    for xs,ys,ws,hs in s:
        cv2.rectangle(roi_img,(xs,ys),(xs+ws,ys+hs),(0,255,0),2)


cv2.imshow("Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()