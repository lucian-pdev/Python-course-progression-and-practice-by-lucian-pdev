print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")
#####################################################################################
# knowledge test

for i in range(1):
    print("#")
else:
    print("#")

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

print(vals)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
print(f"t = {t}")
for i in range(3):
    s += t[i][i]
    print(f"step {i}:{s}")
print(s)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][1])

