import cv2
import numpy as np

img=cv2.imread("Pikachu.png")

kernel=np.ones((5,5), np.uint8)
erosion=cv2.erode(img,kernel)

cv2.imshow("Pika", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()