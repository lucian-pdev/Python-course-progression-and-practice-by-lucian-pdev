# Your task is to write a program which:

#     asks the user for the input file's name;
#     reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#     prints a simple histogram in alphabetical order (only non-zero counts should be presented)

# Create a test file for the code, and check if your histogram contains valid results.

# Assuming that the test file contains just one line filled with:
# aBc
# sample.txt

# the expected output should look as follows:
# a -> 1
# b -> 1
# c -> 1 

# Learner: i prepared an extra samplelarge.txt file, that one is fun
# also, i want to practice Objects

# imports
from os import strerror
from os.path import getsize
import time


# Object practice: class for file metadata handling, 
# class for text files, class for binary handling, class for writing output

# Metadata handler
class filemeta:
    def __init__(self, fname):  
        self.fname = fname
        self.fsize, self.buffer_size = self.find_file(fname)
           
# Getting the file's handle and metadata
    def find_file(self, fname):
        try:
            fsize = getsize(fname)
            buffer_size = 4096 if fsize > 4096 else fsize
            return (fsize, buffer_size)
        except OSError as e:
            print(f"OSError: {strerror(e.errno)}.\n")
            exit(1)

# Text file handler
class ftext(filemeta):
    def __init__(self,fname):
        super().__init__(fname)
        self.__counters = {}

# Open file and parse it
    def open_file(self):
        try:
            start_total = time.perf_counter()
            char_times = {} 
            with open(self.fname, 'r') as fh:
                    for line in fh:
                        for char in line:
                            if char.isalpha():
                                if char != '' or " ":
                                    start = time.perf_counter()
                                    self.histogram_incrementation(char.lower())
                                    end = time.perf_counter()
                                    char_times[char] = end - start
            end_total = time.perf_counter()
            total_time = end_total - start_total
            avg_time = total_time / len(char_times)
            print(f'Average time per character: {avg_time:.9f} seconds.')
            print(f'Total time: {total_time:.6f} seconds.\n')
        except IOError as e:
            print(f'IOError: {strerror(e.errno)}.\n')
            exit(1)

# counters and incrementation
    def histogram_incrementation(self, char):
            if char in self.__counters:
                self.__counters[char] += 1
            else:
                self.__counters[char] = 1

# print histogram in alphabetical order
    def sort_n_print(self):
        to_print = 'In this file there are:'
        for key in sorted(self.__counters.keys()):
            to_print += f'\n{key} -> {self.__counters[key]}'
        to_print += '\n'
        print(to_print)


# main block
if __name__ == "__main__":
    fname = input("\nWhat is the file's path or name?\n>>> ")
    test = ftext(fname)
    test.open_file()
    test.sort_n_print()