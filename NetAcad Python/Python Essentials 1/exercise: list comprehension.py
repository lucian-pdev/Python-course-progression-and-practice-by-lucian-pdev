print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")
#####################################################################################

# squares = [x ** 2 for x in range(10)]
#
# print(squares)
#
# twos = [2 ** i for i in range(8)]
#
# odds = [x for x in squares if x % 2 != 0 ]
#
# print(twos, odds)

#####################################################################################

# matrix = []
#
# for i in range(8):
#     row = [ "-" for j in range(8)]
#     row.append("\n")
#     matrix.append(row)
#
# print(matrix)

#####################################################################################

# temperature reading exercises
import random

temps = [[float(f"{random.randint(0, 40)}.{random.randint(0, 40)}") for h in range(1, 24)] for d in range(1, 31)]
total = 0
for day in temps:
    total += day[11]
print(temps[0][2])
print(temps[0][:])
print(temps[:][2])
average = round(total / 31, 2)
print(temps)

print(f"The average temperature at noon is {average}")

#####################################################################################



