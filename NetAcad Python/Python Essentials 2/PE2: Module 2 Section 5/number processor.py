# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0

if strings == "":
    print("No input detected.")
    exit
try:
    # for substr in strings:
    #     total += float(substr)
    # print("The total is:", total)
    # exit
    total = sum(float(substr) for substr in strings if substr.isdigit() == True)
    print("The total is:", total)
except:
    print("An element is not a number.")
    exit
    