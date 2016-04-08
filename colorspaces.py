import cv2
import numpy as np
import sys

# cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
img = cv2.imread('Images/cokecan.jpg')

# if cap.isOpened(): # try to get the first frame
#     rval, frame = cap.read()
#     frame = cv2.flip(frame, 1)
# else:
#     rval = False

def nothing(x):
    pass

# startR, startBG = 255, 255
# cv2.createTrackbar('R','frame',startR,255,nothing)
# cv2.createTrackbar('BG','frame',startBG,255,nothing)

sR, sBG = 40, 172
cv2.createTrackbar('R_','frame',sR,255,nothing)
cv2.createTrackbar('BG_','frame',sBG,255,nothing)

startKernelSize = 21
cv2.createTrackbar('KS','frame',startKernelSize,101,nothing)

def getCRE(bgrimg):
    grayscale = cv2.cvtColor(bgrimg, cv2.cv.CV_BGR2GRAY)
    ret, thresh_output = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh_output, cv2.cv.CV_RETR_TREE, cv2.cv.CV_CHAIN_APPROX_SIMPLE, (0,0))

    nContours = len(contours)
    minRect = []
    minEllipse = []

    for i in range(nContours):
        c = contours[i]
        minRect.append(cv2.minAreaRect(c))
        if len(c) > 5:
            minEllipse.append(cv2.fitEllipse(c))

    return contours, minRect, minEllipse

def drawEllipses(bgrimg, ellipses):
    for ell in ellipses:
        center, axes, angle = ell
        center = tuple( map(int, center) )
        axes = tuple( map(int, axes) )
        angle = int(angle)
        cv2.ellipse(drawing, center, axes, angle, 0, 360, (255,0,0), 2)

from helpers import *

def drawRectangles(bgrimg, rectangles):
    imgCopy = bgrimg.copy()
    for rect in rectangles:
        box = cv2.cv.BoxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(imgCopy, [box], 0, (0,0,255), -1)
    
    nContours, nRectangles, nEllipses = getCRE(imgCopy)
    for rect in nRectangles:
        box = cv2.cv.BoxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(bgrimg, [box], 0, (0,0,255), 2)

def isCoke(rect):
    sX, sY = sorted(rect[0])
    assert sX <= sY
    if sY <= 2 or sX <= 2:
        return False
    return 2.0 < float(sY) / sX < 2.5 

def drawCokecans(bgrimg, rectangles):
    imgCopy = bgrimg.copy()
    boxes = map(np.int0, map(cv2.cv.BoxPoints, rectangles))
    cv2.drawContours(imgCopy, boxes, 0, (0,0,255), -1)
    newCont, newRect, newEll = getCRE(imgCopy)
    cokes = filter(isCoke, newRect)
    cokeRects = map(np.int0, map(cv2.cv.BoxPoints, cokes))
    cv2.drawContours(bgrimg, cokeRects, 0, (0,0,255), 2)






imgCopy = img
while True: # rval:
    # rval, frame = cap.read()
    # cv2.imshow('frame', frame)

    R = 255 # cv2.getTrackbarPos('R','frame')
    BG = 255 # cv2.getTrackbarPos('BG','frame')
    R_ = cv2.getTrackbarPos('R_','frame')
    BG_ = cv2.getTrackbarPos('BG_','frame')
    
    hsv = cv2.cvtColor(imgCopy, cv2.COLOR_BGR2HSV)
    lower = np.array([BG_,BG_,R_])
    upper = np.array([BG,BG,R])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(imgCopy, imgCopy, mask=mask)

    kernel_size = cv2.getTrackbarPos('KS','frame')
    if kernel_size & 1 == 0:
        kernel_size += 1
    kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
    # dst = cv2.filter2D(res, -1, kernel)
    # dst = cv2.GaussianBlur(res,(kernel_size, kernel_size), 0)
    dst = cv2.medianBlur(res, kernel_size)


    drawingRects = dst.copy()
    drawingCokes = dst.copy()
    contours, rectangles, ellipses = getCRE(drawingRects)
    drawRectangles(drawingRects, rectangles)
    drawCokecans(drawingCokes, rectangles)

    both = (drawingCokes, drawingRects)
    cv2.imshow('frame', np.hstack(both))
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break





cap.release()
cv2.destroyAllWindows()
sys.exit(0)

