#!/usr/bin/env python3

import math

# The new class will be called Triangle and this is what we want:
#     the constructor accepts three arguments – all of them are objects of the Point class;
#     the points are stored inside the object as a private list;
#     the class provides a parameterless method called perimeter(), 
# which calculates the perimeter of the triangle described by the three points; 
# the perimeter is the sum of all the lengths of the legs 
# (we mention this for the record, although we are sure that you know it perfectly yourself.)

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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    # My solution...
    # def perimeter(self):
    #     self.__ab = self.__vertices[0].distance_from_point(self.__vertices[1])
    #     self.__bc = self.__vertices[1].distance_from_point(self.__vertices[2])
    #     self.__ac = self.__vertices[2].distance_from_point(self.__vertices[0])
    #     self.__perimeter = self.__ab + self.__bc + self.__ac
    #     return self.__perimeter
    
    # Course's solution.... yeah, more versatile
    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    
    
class MakeTriangles(Triangle, Point):
    """Assemble a list of triangles from a given list of coordinates.
    The list must have 6 numerical values per triangle."""
    def __init__(self, *args):
        # assemble the vertices of each triangle from argument list
        self.__vertices = []
        if len(args) % 2 == 0:
            for i in range(0, len(args), 2):
                temp_point = args[i:i+2]
                self.__vertices.append(Point(temp_point[0], temp_point[1]))
        else:
            print("This operation demands 2 numerical values per point.")
            exit("Program clossing.")
        
        # make the triangles
        self.__triangles = []
        for a in range(0, len(self.__vertices), 3):
            vertices = self.__vertices[a:a+3]
            if len(vertices) == 3:
                self.__triangles.append(Triangle(vertices[0], vertices[1], vertices[2]))
            else:
                break
  
    
    def __str__(self):
        result = "Stored triangles:\n"
        for i, triangle in enumerate(self.__triangles, 1):
            verts = triangle._Triangle__vertices  # Accessing the private attribute
            coords = [(v.getx(), v.gety()) for v in verts]
            result += f"  Triangle {i}: {coords}\n"
        return result
    
        
arg = []
for a in range(1,105,4):
    arg.append(a)
    
print(arg)
print(len(arg))

triangleAlpha = MakeTriangles(*arg)
print(triangleAlpha)