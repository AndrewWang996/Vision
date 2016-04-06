import cv2

cv2.namedWindow("preview")
cv2.namedWindow("drawing")

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
    drawFrame = frame.copy()
else:
    rval = False

radius = 41 # radius in pixels
drawRadius = 10

while rval:
    #cv2.imshow("preview", frame)

    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply a Gaussian blur to the image then find the brightest
    # region
    gray = cv2.GaussianBlur(gray, (radius, radius), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    R,G,B = map(int, frame[maxLoc[1]][maxLoc[0]])
    perceivedBrightness = (R+R+R+B+G+G+G+G)>>3
    
    if perceivedBrightness > 200:
        cv2.circle(drawFrame, maxLoc, drawRadius, (255, 0, 0), -1)
    
    # display the results of our newly improved method
    # cv2.imshow("preview", frame)
    cv2.imshow("drawing", drawFrame)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")




'''
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
 
# load the image and convert it to grayscale
print args['image']
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# apply a Gaussian blur to the image then find the brightest
# region
gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 2)
 
# display the results of our newly improved method
cv2.imshow("Robust", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
