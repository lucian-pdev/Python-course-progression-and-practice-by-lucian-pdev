# Your task is to write a program which:

#     asks the user for Prof. Jekyll's file name;
#     reads the file contents and counts the sum of the received points for each student;
#     prints a simple (but sorted) report, just like this one:
# Andrew   Cox      1.5
# Anna     Boleyn   15.5
# John     Smith    7.0 

# Note:

#     your program must be fully protected against all possible failures: 
# the file's non-existence, the file's emptiness, or any input data failures; 
# encountering any data error should cause immediate program termination, 
# and the error should be presented to the user;
#     implement and use your own exceptions hierarchy – we've presented it in the editor; 
# the second exception should be raised when a wrong line is detected, 
# and the third when the source file exists but is empty.

# Tip: Use a dictionary to store the students' data.

from os import strerror

class StudentsDataException(Exception):
    def __init__(self, message='General issue with the data.'):
        Exception.__init__(self, message)               # when exceptions are called this will make sure they are treated as such
                                                        # because i don't know how to write an exception from the ground up yet
        
    def __str__(self, message='error not handled'):
        return f"Something is wrong with this information:{message}."

class BadLine(StudentsDataException):
    def __init__(self, message='line is incorrect'):
        StudentsDataException.__init__(self, message)       # invoking parent constructor
    
    def __str__(self, message='[Error] exception not handled'):
        return f'This line <<{message}>> is incorrect. 0 points!\n'

class FileEmpty(StudentsDataException):
    def __init__(self, message=f'This file is empty. 0 points!\n'):
        super().__init__(message)                           # invoking parent constructor differently
        
    def __str__(self):
        return f'This file is empty. 0 points!\n'

fname = input("What's the file's name?\n>>> ")

list_of_dicts = []

try:
    stream = open(fname,'rt')
    line = stream.readline()        # first buffer
    while True:   
                                    # main loop
        if line != '':              # continue if not EOF
            line = line.split()     # break line into words
            if len(line) == 3:
                if not any(x['name'] == line[0] and x['surname'] == line[1] for x in list_of_dicts):
                    # any checks if any of the conditions is true
                    # 2 conditions to checks name and surname match with the data in the buffer
                    # list comprehension to let me iterate over all the indexes in the list
                    list_of_dicts.append(dict(name=line[0],surname=line[1],score=line[2]))
                    line = stream.readline()        # refill buffer
                else:
                    for x in range(len(list_of_dicts)):
                        if list_of_dicts[x]['name'] == line[0] and list_of_dicts[x]['surname'] == line[1]:
                            list_of_dicts[x]['score'] = float(list_of_dicts[x]['score']) + float(line[2])
                    line = stream.readline()        # refill buffer
            else:
                print(f'This: {line}\n')
                raise BadLine(' '.join(line))
        else:
            break
        
    stream.close()

    if len(list_of_dicts) == 0:     # check if file is empty
        raise FileEmpty
    
    sorted_list = sorted(list_of_dicts, key=lambda x: x['name'])
    
    print('\nResults:')
    for student in sorted_list:
        print(f'{student["name"]} {student["surname"]} {student["score"]}')
    
except FileEmpty as e:
    print(e)
except BadLine as e:
    print(e)
except StudentsDataException as e:
    print(e)
except IOError as e:
    print(f'IOError: {strerror(e.errno)}')