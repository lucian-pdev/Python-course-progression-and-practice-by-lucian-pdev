
    # asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
    # add all digits together and if it has more than 1 digit, add them up again
    # outputs the Digit of Life for the date.

def digit_of_life():
    user_input = input("Enter your birthday in the format YYYYMMDD or DDMMYYYY:")
    formatted_input = user_input.strip()
    total = 0
    if formatted_input.isdigit():
        for i in formatted_input:
            total += int(i)
        while len(str(total)) > 1:
            ftotal = 0
            for i in str(total):
                ftotal += int(i)
            total = ftotal
        else:
            print(total)
            return
        print(total)
    else:
        print("Invalid input. Please enter your birthday in the format YYYYMMDD or DDMMYYYY.")
        return
        
        
if __name__ == "__main__":
    digit_of_life()