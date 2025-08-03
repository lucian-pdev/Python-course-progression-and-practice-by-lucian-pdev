print("""The comment line shortcut is CTRL+/.
The interrupt hotkey is CTRL+C/CTRL+break.
""")


#####################################################################################
# LAB: Leap year exercise with function

def is_year_leap(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

#####################################################################################
# LAB   How many days: writing and using your own functions

# def is_year_leap(year):
#
# Your code from the previous LAB.
#

def days_in_month(year, month):
    if is_year_leap(year):
        february = 29
    else:
        february = 28
    list_days_in_month = [None, 31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return list_days_in_month[month]


# test_years = [1900, 2000, 2016, 1987, 4500, 8857]
# test_months = [2, 2, 1, 11, 0, 2]
# test_results = [28, 29, 31, 30, None, 28]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

#####################################################################################
# LAB: Your task is to write and test a function which takes three arguments
# (a year, a month, and a day of the month) and returns the corresponding day of the year,
# or returns None if any of the arguments is invalid.

# def is_year_leap(year):
#
# Your code from the previous LAB.
#

# def days_in_month(year, month):
#
# Your code from the previous lab.
#

def day_of_year(year=2000, month=1, day=1):
    adding_days_up = 0
    for m in range(1, month):
        adding_days_up += days_in_month(year, m)
    adding_days_up += int(day)
    return adding_days_up


def request_arguments_for_explicit_date():  # only usable with day_of_the_year funct.
    year = int(input("Requesting data: What year?"))
    month = int(input("Requesting data: Which month (numerical) ?"))
    day = int(input("Requesting data: Which day of the month (numerical) ?"))
    return day_of_year(year, month, day)


def english_ordinal_number_suffix(number):
    string_number = str(number)
    last_digit = int(string_number[-1])
    if last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return str(number) + suffix  # Warning: string type output


# print(f"That day is {day_of_year(2000, 12, 27)} of the year.")
# print(f"That day is the {english_ordinal_number_suffix(request_arguments_for_explicit_date())} of the year.")

#####################################################################################
# LAB: finding prime numbers
def is_prime(num):
    if num < 2:
        return False
    sqr_root = int(round(num ** 0.5, 0))
    for n in range(2, sqr_root + 1):
        if num % n == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print("\n")
#####################################################################################
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres
hundred_km_to_miles = 100_000 / 1_609.344
gallons_ratio = 3.785411784

def liters_100km_to_miles_gallon(liters):
    mpg = (hundred_km_to_miles * gallons_ratio) / liters
    return mpg

def miles_gallon_to_liters_100km(miles):
    lp100k = (hundred_km_to_miles * gallons_ratio) / miles
    return lp100k

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# think tank below

# convert distance
# hundred_km_to_miles = 100_000 / 1_609.344
# from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key

# convert fuel
# liters = 3.9
# gallons_ratio = 3.785411784
# gallons = liters / gallons_ratio
# mpg = (hundred_km_to_miles * gallons_ratio) / liters
# given_mpg = 62
# lp100k = (hundred_km_to_miles * gallons_ratio) / given_mpg
# print(mpg)
# print(lp100k)
#
# print(f"""{hundred_km_to_miles} / ({liters} / {gallons_ratio}) = \n
# {hundred_km_to_miles} / {liters / gallons_ratio} =\n
# {hundred_km_to_miles / (liters / gallons_ratio)}
# """)

# check 2 sha_1

# sha_1_A = str(input("Paste the first sha."))
# sha_1_B = str(input("Paste the second sha."))
#
# if sha_1_A == sha_1_B:
#     print(f"All good.")
# else:
#     print(f"Those are not same.")

