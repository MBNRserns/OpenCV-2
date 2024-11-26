import cv2

img1=cv2.imread("Ash.png")
img2=cv2.imread("Pikachu.png")

addImage=cv2.addWeighted(img1,0.5,img2,0.4, 0)

cv2.imshow("Duo",addImage)

cv2.waitKey(0)
cv2.destroyAllWindows()