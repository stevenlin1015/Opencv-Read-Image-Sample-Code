import cv2 as cv

img = cv.imread("/Users/stevenlin/Downloads/bmw_m5.jpg", 1) #please change image path you like
resized_image = cv.resize(img, (800, 450))
cv.imshow("BMW M5 image", resized_image)
cv.waitKey(0)
cv.destroyAllWindows()