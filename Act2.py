import cv2

img1=cv2.imread("Ash.png")
img2=cv2.imread("Pikachu.png")

sub=cv2.subtract(img1,img2)

cv2.imshow("Duo",sub)

cv2.waitKey(0)
cv2.destroyAllWindows()