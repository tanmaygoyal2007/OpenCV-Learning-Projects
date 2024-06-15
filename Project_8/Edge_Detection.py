import cv2
img=cv2.imread("photos/cat1.jpg")
img=cv2.resize(img,(500,500))

new_img=cv2.Canny(img,50,50,apertureSize=5,L2gradient=False)

cv2.imshow("Cat",new_img)
cv2.imshow("Cat1",img)

cv2.waitKey(0)
cv2.destroyAllWindows()