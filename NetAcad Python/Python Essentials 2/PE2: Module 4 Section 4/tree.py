#!/usr/bin/env python3

# Your program should meet the following requirements:

#     Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
#     The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.

import os

# os.chdir('./NetAcad Python/Python Essentials 2/PE2: Module 4 Section 4')
print(f'\nCurrent directory: {os.getcwd()}.\nFiles in current directory: {os.listdir(os.getcwd())}.\n')

    
# TODO: make a temporary list of the paths identified in the working dir. 
# String manipulation to make the new paths, list dir offers only the names inside the given path
# so: paths.append ( cwd + os.path.sep + os.listdir ) 
# search in each subdir
# find elem related to given dir name
# compare the new results of listdir with given dir for find
# append good results in dict with incremented index = path (string manipulation)
# return the full dictionary of results as a nicely formatted string to terminal


def find(dir, path=os.getcwd()):
    print(os.system(f"find '{path}' -type d -name '{dir}'"))
    

# find('python')

# def find(dir, path=os.getcwd(), sep=os.path.sep):
#     print(x + '\n' for x in [find(dir, path=os.listdir(item)) for item in os.listdir(str(path)) if os.path.isdir(path + sep + item)])

find('python')

print("---"*20)

def find(dir, path=os.getcwd(), sep=os.path.sep):
    try:
        for i in os.listdir(path):
            print(path + sep + i + '\n' if i == dir else "", end='')
            find(dir, path=path+sep+i)
    except (PermissionError, FileNotFoundError, NotADirectoryError):
        pass

        
        
find('python') 
            