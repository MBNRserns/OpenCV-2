import cv2

img=cv2.imread("Pikachu.png")

resized=cv2.resize(img, (500,250))
cv2.imshow("Pika",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()