print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")

# Bitwise operations

g = 29
y = 23

print("x & y =", g & y)
print("x | y =", g | y)
print("x ^ y =", g ^ y)

print("x << 5 =", g << 5)      # 29 * 2 ** 5
print("y >> 3 =", y >> 3)      # 23 // ( 2 ** 3 )

g = 0

g |= (1 << 4)
print(g)       # bit is 0, then compared in OR with a 1, the 1 wins, bit is set

g &= ~(1 << 4)
print(g)        # bit is 1, compared with negated 1 ( bit 0 ), only 1 is positive, thus fails, bit is reset

g ^= (1 << 2)   # bit is 0, because XOR toggles a value if compared with the opposite, it turns to 1
print(g)

g ^= (1 << 2)
print(g)


# random x at different locations via bit flag coordinates with 1 sec timer
import random
import time

x_axis = 0

# function: checks if the bit in var x, at position pos is set
def is_bit_set(x,pos):
    return (x & (1 << pos)) != 0

def line_maker(x):
    printing_space = ""
    for space in range(0,7):
        if is_bit_set(x,space) == True:
            printing_space += "x"
        else:
            printing_space += "_"
    return printing_space

# Check if the bit at position 3 is set in 29 (0b11101)
print("Is bit 3 set in 29?", is_bit_set(29, 3))

to_print = "a"
to_print += "bc"
print(to_print)

for timer in range(0,10):
    x_axis = 0
    mask = random.randint(0,7)
    x_axis |= (1 << mask)
    x_axis = line_maker(x_axis)
    print(x_axis)
    time.sleep(1)
