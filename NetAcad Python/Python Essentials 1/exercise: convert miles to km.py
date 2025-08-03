print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")

john = 3
adam = 6
mary = 5
total_apples = john + mary + adam
print(john, adam, mary, total_apples, sep=",")

kilometers = 12.25
miles = 7.38

# 1 mile = 1.61 km

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Task: y = 3x^3 - 2x^2 + 3x - 1

# Hardcode your test data here.
# sample input
# x = 0
# x = 1
x = -1
x = float(x)
# Write your code here.
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)

a=float(input("Give me a value for a: "))
# input a float value for variable b here
b=float(input("Give me a value for b:"))
# output the result of addition here
print(a+b)
# output the result of subtraction here
print(a-b)
# output the result of multiplication here
print(a*b)
# output the result of division here
print(a/b)
print("\nThat's all, folks!")

x = float(input("Enter value for x: "))

# Write your code here.
y=1/(x+(1/(x+(1/(x+1/x)))))
print("y =", y)

