print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")

# comparison operators

# n = int(input("Give cookie:"))
# print(n>=100)

# Condition: if-elif-else statements

# user_input = str(input("What flower did you bring?"))
# if user_input == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best")
# elif user_input == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not ", user_input, "!", sep="")
# exit(0)

# Exercise 1

# income = float(input("Enter the annual income: "))
#
# if income < 85528:
#     tax = income * 0.18 - 556.02
# # Write the rest of your code here.
# else:
#     tax = 14839.2 + ((income-85528)*0.32)
#
# tax = round(tax, 0)
# if tax > 0:
#     print("The tax is:", tax, "thalers")
# else:
#     print("The tax is: 0.0 thalers")
# exit(0)

# Exercise 2

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if (year % 4) > 0:
        print("Common year")
    elif (year % 100) > 0:
        print("Leap year")
    elif (year % 400) > 0:
        print("Common year")
    else:
        print("Leap year")
