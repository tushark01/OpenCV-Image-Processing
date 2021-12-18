import cv2

img = cv2.imread("barbara.jpg")
height = img.shape[0]
width = img.shape[1]

#cv2.line(img, (0,0), (0,650), (0,0,255), 10)
#cv2.line(img, (650,0), (0,650), (0,0,255), 10)
#draw arrowde line
#draw rectangle
#draw circle

#cv2.rectangle(img, (100,100), (500,500), (127,0,255), 10)
center_coordinates = (250, 250)
 
# Radius of circle
radius = 100
  
# Blue color in BGR
color = (150, 0, 150)
  
# Line thickness of 2 px
thickness = 5


image = cv2.circle(img, center_coordinates, radius, color, thickness)

#line 

cv2.imshow("Image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()