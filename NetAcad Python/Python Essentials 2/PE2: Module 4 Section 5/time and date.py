# Write a program that creates a datetime object for November 4, 2020 , 14:53:00. 
# The object created should call the strftime method with the appropriate format to display the following result:
# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44 
# Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.

import datetime, time

obj = datetime.datetime(year=2020, month=11, day=4, hour=14, minute=53, second=00)
# or 
obj2 = datetime.datetime(2020, 11, 4, 14, 53, 00)

print("\n")
print(obj.strftime("%Y/%m/%d %H:%M:%S"))
print(obj.strftime("%y/%B/%d %H:%M:%S %p"))
print(obj.strftime("%a, %Y %b %d"))
print(obj.strftime("%A, %Y %B %d"))
print(obj.strftime("Weekday: %w"))
print(obj.strftime("Day of the year: %j"))
print(obj.strftime("Week number of the year: %W"))

print(obj2.strftime("%Y/%m/%d %H:%M:%S"))
print(obj2.strftime("%y/%B/%d %H:%M:%S %p"))
print(obj2.strftime("%a, %Y %b %d"))
print(obj2.strftime("%A, %Y %B %d"))
print(obj2.strftime("Weekday: %w"))
print(obj2.strftime("Day of the year: %j"))
print(obj2.strftime("Week number of the year: %W"))