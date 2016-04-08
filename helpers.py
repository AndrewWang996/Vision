

import numpy as np
import cv2

# Return strue if a point is located within a rotated rectangle
def pointInRectangle(point, rect):
    px,py = point
    sortedVertices = sortCounterclockwise(rect)

def intersect(rect1, rect2):
	for p1 in rect1:
		if pointInRectangle(p1, rect2):
			return True
	for p2 in rect2:
		if pointInRectangle(p2, rect1):
			return True
	return False

def getMinUnionRect(rect1, rect2):
	return cv2.minAreaRect(np.hstack(rect1, rect2))

# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
def ccw(p1, p2, p3):
	return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

# Take a list of points and return a new list sorted in counterclockwise order
def sortCounterclockwise(pts):
	points = pts.tolist()
	return [points[0]] + sorted(points[1:], cmp=lambda a,b: ccw(points[0],a,b))


def mergeRectangles(rectangles):
	nRect = len(rectangles)
	for i in range(nRect):
		for j in range(i):
			if intersect(rectangles[i], rectangles[j]):
				pass




