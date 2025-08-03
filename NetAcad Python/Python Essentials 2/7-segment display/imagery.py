#!/usr/bin/env python3

def seven_segment_display(i=0):
    """Returns images for a 7-segment display made of #.
        Valid arguments (string): line, left, right, sides"""
    images = ["###","#  ","  #","# #"]
    valid_args = ["line","left","right","sides"]
    if i not in valid_args:
        return "Incorrect argument. Must be INT:0-10."
    if i == "line":
        return images[0]
    elif i == "left":
        return images[1]
    elif i == "right":
        return images[2]
    elif i == "sides":
        return images[3]
    else:
        return None
    
if __name__=="__main__":
    print("This module is an image library for a 7-segement display using #s in python.")
    exit