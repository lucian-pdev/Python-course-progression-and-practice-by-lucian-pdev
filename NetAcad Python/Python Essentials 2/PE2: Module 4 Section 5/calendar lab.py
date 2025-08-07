# Your task now is to extend its functionality with a new method called count_weekday_in_year,
# which takes a year and a weekday as parameters,
# and then returns the number of occurrences of a specific weekday in the year.

# Use the following tips:

#     Create a class called MyCalendar that extends the Calendar class;
#     Create the count_weekday_in_year method with the year and weekday parameters.
#       The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
#       The method should return the number of days as an integer;
#     In your implementation, use the monthdays2calendar method of the Calendar class.

# The following are the expected results:
# Exp inp: year=2019, weekday=0
# Exp out: 52

import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()
    
    def count_weekday_in_year(self, year, weekday):
        count = 0
        if weekday not in (0,1,2,3,4,5,6):
            return f"{weekday} is an invalid weekday integer."
        for month in range (1,13):    
            for week in self.monthdays2calendar(year, month):
                for monthdaynum, weekdaynum in week:
                    if weekdaynum == weekday and monthdaynum != 0:
                        count += 1
        return count

cal = MyCalendar()
print(cal.count_weekday_in_year(2019, 0))

# test
# c = calendar.Calendar()
# print(c.monthdays2calendar(2019, 1))

