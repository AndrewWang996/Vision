import numpy as np
import cv2
import sys


cv2.namedWindow("drawing")

img = cv2.imread('Images/circles.jpg')

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red_hue_range = cv2.inRange(hsv_image, (0,100,100), (10,255,255))
upper_red_hue_range = cv2.inRange(hsv_image, (160,100,100), (179,255,255))
red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0,
                                upper_red_hue_range, 1.0, 0)
red_hue_image = cv2.GaussianBlur(red_hue_image, (9,9), 2, 2)

circles = cv2.HoughCircles(red_hue_image, cv2.cv.CV_HOUGH_GRADIENT, 1, len(red_hue_image) / 8, 100, 20, 50)

if len(circles) == 0:
    sys.exit(0)
for circle in circles[0]:
    print circle
    center = (circle[0], circle[1])
    radius = circle[2]
    cv2.circle(img, center, radius, (0,255,0), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
else:
    rval = False
'''




'''
while rval: 

    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)


    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red_hue_range = cv2.inRange(hsv_image, (0,100,100), (10,255,255))
    upper_red_hue_range = cv2.inRange(hsv_image, (160,100,100), (179,255,255))
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0,
                                    upper_red_hue_range, 1.0, 0)
    
    cv2.imshow("drawing", red_hue_image)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
'''


cv2.destroyAllWindows()










