#!/usr/bin/env python3

import imagery
import os


def joining_images(sequence):
    """Returns a string with the images of a 7-segment display for the given sequence.
       Valid arguments: int."""
    if not sequence.isdigit():
        return "Incorrect argument. Must be INTEGER."
    positional_dict = {}
    stringy = str(sequence)
    for i in stringy:
        positional_dict[i] = {"top_key":None, 
                             "top_middle":None, 
                             "middle_key":None, 
                             "bottom_middle":None, 
                             "bottom_key":None}
    for i in stringy:
        if i == "0":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("sides")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "1":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("right")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("right")
        elif i == "2":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("left")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "3":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "4":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("sides")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("right")
        elif i == "5":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("left")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "6":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("left")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "7":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("right")
        elif i == "8":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        elif i == "9":
            positional_dict[i]["top_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["top_middle"] = imagery.seven_segment_display("sides")
            positional_dict[i]["middle_key"] = imagery.seven_segment_display("line")
            positional_dict[i]["bottom_middle"] = imagery.seven_segment_display("right")
            positional_dict[i]["bottom_key"] = imagery.seven_segment_display("line")
        else:
            return "Woops."
    for line in range(5):
        line_in_progress = ""    
        for x in stringy:
            line_in_progress += positional_dict[x]["top_key"] if line == 0 else \
                                positional_dict[x]["top_middle"] if line == 1 else \
                                positional_dict[x]["middle_key"] if line == 2 else \
                                positional_dict[x]["bottom_middle"] if line == 3 else \
                                positional_dict[x]["bottom_key"]
            line_in_progress += " "
        print(line_in_progress)
            




if __name__ == "__main__":
    os.system('clear')  # Clear the terminal screen for better visibility
    joining_images(input("Enter a number: "))
    exit