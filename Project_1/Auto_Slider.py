import cv2
import os
list_name=os.listdir("photos")
for name in list_name:
    path="photos"
    img_name=path + '//' + name
    img=cv2.imread(img_name)
    img=cv2.resize(img,(500,600))
    cv2.imshow("cat",img)
    cv2.waitKey(1500)
cv2.destroyAllWindows()

