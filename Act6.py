import cv2

img=cv2.imread("Pikachu.png")
cv2.imshow("Original",img) 

gaussian=cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("Gaussian Blur",gaussian)

median=cv2.medianBlur(img,5)
cv2.imshow("Median Blur",median)

bilateral=cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral Blur",bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
#(img, Kernal_size ,std_dev)
# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.
#(img,Kernal_size)
# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)