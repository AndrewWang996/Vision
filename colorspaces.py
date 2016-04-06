import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

if cap.isOpened(): # try to get the first frame
    rval, frame = cap.read()
    frame = cv2.flip(frame, 1)
else:
    rval = False

def nothing(x):
    pass

startR, startBG = 255, 255
cv2.createTrackbar('R','frame',startR,255,nothing)
cv2.createTrackbar('BG','frame',startBG,255,nothing)

sR, sBG = 40, 172
cv2.createTrackbar('R_','frame',sR,255,nothing)
cv2.createTrackbar('BG_','frame',sBG,255,nothing)

while rval:
    rval, frame = cap.read()
    cv2.imshow('frame', frame)

    R = cv2.getTrackbarPos('R','frame')
    BG = cv2.getTrackbarPos('BG','frame')
    R_ = cv2.getTrackbarPos('R_','frame')
    BG_ = cv2.getTrackbarPos('BG_','frame')
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([BG_,BG_,R_])
    upper = np.array([BG,BG,R])

    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel_size = 11
    kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
    # dst = cv2.filter2D(res, -1, kernel)
    # dst = cv2.GaussianBlur(res,(kernel_size, kernel_size), 0)
    dst = cv2.medianBlur(res, kernel_size)

    ret, thresh = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('frame', thresh)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
sys.exit(0)

