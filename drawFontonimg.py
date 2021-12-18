import cv2

img = cv2.imread("barbara.jpg")
cv2.putText(img, "Hii! Barbara ", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 4)

	
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()