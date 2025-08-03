try:
    temperature = float(input('Enter current temperature:'))
    if type(temperature) != float:
        print(f"Please write a number using only 0-9 digits, no other type of symbols.")
    if temperature > 0:
        print("Above zero")
    elif temperature < 0:
        print("Below zero")
    else:
        print("Zero")
except:
    print(f"Something is wrong, please contact customer support.")