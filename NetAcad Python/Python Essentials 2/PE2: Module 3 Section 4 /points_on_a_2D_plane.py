#!/usr/bin/env python3

import math

# for this exercise:
# all properties must be private

class Point:
    """Store and evaluate Cartesian coordinates in a 2D plane."""
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        """Evaluate distance from this object's point to a given coordinate."""
        x = abs(self.__x - float(x))
        y = abs(self.__y - float(y))
        return math.hypot(x, y)
        
    def distance_from_point(self, point):
        """Evaluate the distance from this object's point to another Point class object."""
        x = point.getx()
        y = point.gety()
        x = abs(self.__x - x)
        y = abs(self.__y - y)
        return math.hypot(x, y)

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point1.distance_from_point(point2) == 1.4142135623730951)
    print(point2.distance_from_xy(2, 0))
    print(point2.distance_from_xy(2, 0) == 1.4142135623730951)
    