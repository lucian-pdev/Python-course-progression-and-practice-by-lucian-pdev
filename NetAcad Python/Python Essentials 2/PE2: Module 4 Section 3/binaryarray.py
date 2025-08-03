from os import strerror
from random import randint

stringus = "I wish i had a job..."
sample = []

for char in stringus:
    sample.append(ord(char))

# for i in range(25):
#     sample.append(randint(0,255))

data = bytearray(sample)


try:
    bf = open('learn_binary_array.bin', 'wb')
    bf.write(data)
    bf.close()
    
    
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.

reading_sample = bytearray(250)


try:
    rbf = open('learn_binary_array.bin', 'rb')
    rbf.readinto(reading_sample)
    rbf.close()
    
    line = []
    
    print(f"\nIntrospective print, if rbf exists: {type(rbf)}")

    print(f'\nItems as-is:hex:chr in reading_sample:\n')
    for item in reading_sample:
        if item != 0:
            print(f'{item}:{hex(item)}:{chr(item)} ', end='')
            line.append(chr(item))
        else:
            continue
    print('\n')
        
    print(f'\nFull line print:"{''.join(line)}"\n')
        
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    