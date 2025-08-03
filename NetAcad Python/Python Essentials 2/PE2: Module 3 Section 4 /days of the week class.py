class WeekDayError(Exception):
    pass
	

class Weeker:
    """A class to represent and calculate days of the week."""
    # Tuple for immutable list of day names
    day_names = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")

    def __init__(self, day):
        """Constructor to handle the 'out of scope'-WeekDayError exception
        and set the main variable __day."""
        if day not in Weeker.day_names:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        """Return the main value as string.""" 
        return str(self.__day)

    def add_days(self, n):
        """Add n days."""
        index = Weeker.day_names.index(self.__day)
        index = (index + n) % 7
        self.__day = Weeker.day_names[index]

    def subtract_days(self, n):
        """Subctrat n days."""
        index = Weeker.day_names.index(self.__day)
        index = (index - n) % 7
        self.__day = Weeker.day_names[index]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    