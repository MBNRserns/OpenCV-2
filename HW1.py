import cv2
import numpy as np

img1=cv2.imread("Gohan.jpg")
img2=cv2.imread("Piccolo.jpg")

addImage=cv2.addWeighted(img1,0.5,img2,0.4,0)

cv2.imshow("Add",addImage) 

subImage=cv2.subtract(img1,img2)

cv2.imshow("Subtract",subImage) 

kernel=np.ones((5,5), np.uint8)
Erosion=cv2.erode(img1,kernel)

cv2.imshow("Erosion",Erosion) 

Resize=cv2.resize(img1,(500,250))

cv2.imshow("Resize",Resize) 

cv2.waitKey(0)
cv2.destroyAllWindows()