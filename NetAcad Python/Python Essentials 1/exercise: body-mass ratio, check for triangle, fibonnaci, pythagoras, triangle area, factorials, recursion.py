# Practice functions: multi-parameter functions
#WARNING RECURSION THEORY AT THE END

# body to mass ratio
def lb_to_kg(lb):
    return lb * 0.45359237


def feet_and_inch_to_meter(feet, inch=0.0):
    return feet * 0.3048 + inch * 0.0254


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return round(weight / height ** 2, 2)


print(f"European measurements: {bmi(352.5, 1.65)}")
print(f"American measurements: {bmi(weight=lb_to_kg(176), height=feet_and_inch_to_meter(5, 7))}")


# can it be a triangle?
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

if is_a_triangle(1, 1, 3):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')


# pythagorean theorem
# c**2 = a**2 + b**2
def is_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    return a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2


print(is_right_triangle(5, 3, 4))


# evaluating a triangle's area
# Heron's formula
# s = (a + b + c) / 2
# A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# x ** 0.5 = root(x)

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(area_of_triangle(1., 1., 2. ** .5))

# factorials
# 0! = 1 ; 1! = 1 ; 2! = 1 * 2
# n! = n * (n-1) * (n-2) * ... * 1

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    factorial_n = 1
    for num in range(1,n+1):
        factorial_n *= num
        # print(f"Testing code:{factorial_n}")
    return factorial_n

for x in range(1,6):
    print(f"Factorial function check: sample {x}, result:{factorial_function(x)}.")

# Fibonacci sequence
# A sequence of integer numbers built using a very simple rule:
#     the first element of the sequence is equal to one (Fib1 = 1)
#     the second is also equal to one (Fib2 = 1)
#     every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)
# Golden Ratio "φ"
#   The ratio of two consecutive numbers is called Golden Ratio ( a / (a+1) )
#   Often appears in nature, in architecture creates pleasing art-pieces and impressive buildings

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

#WARNING ## RECURSION ##
# Recursion is a technique where a function invokes itself.
# Risk involved. If you forget to consider the conditions
# which can stop the chain of recursive invocations,
# the program may enter an infinite loop.
# Recursive calls consume a lot of memory!!!

# Fibonacci recursion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# Factorial recursion
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


