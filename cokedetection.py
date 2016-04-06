import cv2
import cv2.cv as cv
import time
coke_cascade = cv2.CascadeClassifier('Classifiers/haarcascade_coke2.xml')
img = cv2.imread('Images/cokecan.jpg')
cv2.namedWindow('img')
rejectLevels = []
levelWeights = []
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass
startA = 100
startB = 200
cv2.createTrackbar('MIN','img',startA,1000,nothing)
cv2.createTrackbar('MAX','img',startB,1000,nothing)

img2 = img
while True:
    cv2.imshow('img',img2)
    
    k = cv2.waitKey(20)
    if k == 27:
        break
    
    a = cv2.getTrackbarPos('MIN','img')
    b = cv2.getTrackbarPos('MAX','img')
    
    cokes = coke_cascade.detectMultiScale(gray,rejectLevels,levelWeights, 1.1, 3, cv.CV_HAAR_FIND_BIGGEST_OBJECT,(a,a),(b,b),True)
    img2 = img.copy()
    for (x,y,w,h) in cokes:
        cv2.rectangle(img2, (x,y), (x+w, y+h), (255,0,0), 2)
    

key = cv2.waitKey(2000)
cv2.destroyAllWindows()



import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Classifiers/haarcascade_eye.xml')
coke_cascade = cv2.CascadeClassifier('Classifiers/haarcascade_coke2.xml')

cv2.namedWindow("drawing")


'''
img = cv2.imread('Images/sodas.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cokes = coke_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in cokes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''





vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)
else:
    rval = False


while rval: 

    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cokes = coke_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in cokes:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow("drawing", frame)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyAllWindows()

