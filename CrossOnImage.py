import cv2

img = cv2.imread("barbara.jpg")
height = img.shape[0]
width = img.shape[1]

cv2.line(img, (0,0), (700,700), (0,0,255), 10)
cv2.line(img, (650,0), (0,650), (0,0,255), 10)


#line 

cv2.imshow("Image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()