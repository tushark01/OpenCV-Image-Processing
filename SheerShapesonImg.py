import cv2

img = cv2.imread("barbara.jpg")


center_coordinates = (250, 250)
  
axesLength = (190, 150)
angle = 270
startAngle = 0
endAngle = 360
color = (255,255,86)
   
# Line thickness of 5 px
thickness = 10

image = cv2.ellipse(img, center_coordinates, axesLength,
           angle, startAngle, endAngle, color, thickness)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()