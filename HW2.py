import cv2

#BORDERING
img=cv2.imread("Gohan.jpg")
Border=cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_ISOLATED,value= 1)
cv2.imshow("Bordered Image",Border)

#BLURRING
gaussian=cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("Gaussian Blur",gaussian)

median=cv2.medianBlur(img,5)
cv2.imshow("Median Blur",median)

bilateral=cv2.bilateralFilter(img, 9,75,75)
cv2.imshow("Bilateral Blur",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()