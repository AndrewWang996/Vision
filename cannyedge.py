import numpy as np
import cv2
from matplotlib import pyplot as plt

startA = 100
startB = 200
img = cv2.imread('Images/larry.jpg')
edges = cv2.Canny(img,startA,startB)

def nothing(x):
    pass

cv2.namedWindow('img')
cv2.createTrackbar('A','img',startA,1000,nothing)
cv2.createTrackbar('B','img',startB,1000,nothing)


while True:
    cv2.imshow('img', edges)
    k = cv2.waitKey(20)
    if k == 27:
        break
    a = cv2.getTrackbarPos('A','img')
    b = cv2.getTrackbarPos('B','img')
    edges = cv2.Canny(img,a,b)

print 'destroying all windows'
cv2.destroyAllWindows()

