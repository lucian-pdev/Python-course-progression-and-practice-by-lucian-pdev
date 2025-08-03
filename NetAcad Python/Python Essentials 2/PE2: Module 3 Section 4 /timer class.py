#!/usr/bin/env python3

# timer class, the constructor accepts 3 variables:
# hours, minutes and seconds, in military time, with default 0
# no need for validation checks
# objects of the class should be printable, implicitly convert themselves into strings,
# in format "hh:mm:ss", with leading 0s for values < 10
# define the parameterless methods next_second() and previous_second()
# incremeting the time +/- 1
# all object properties should be printable
# consider a separate function (not method!) to format the time string


class Timer:
    """
    A 24-hour clock timer storing hours, minutes, and seconds.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """Initialize with optional hours, minutes, seconds (all ints)."""
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def __str__(self):
        """Return time as 'hh:mm:ss' with leading zeros."""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        """
        Increment the timer by one second, rolling over at 60s, 60m, 24h.
        Returns self to allow chaining.
        """
        total = self.hours * 3600 + self.minutes * 60 + self.seconds + 1
        total %= 24 * 3600
        self.hours, remainder = divmod(total, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        return self

    def previous_second(self):
        """
        Decrement the timer by one second, rolling backward at 0s, 0m, 0h.
        Returns self to allow chaining.
        """
        total = self.hours * 3600 + self.minutes * 60 + self.seconds - 1
        total %= 24 * 3600
        self.hours, remainder = divmod(total, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
        return self



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)

print(timer.__dict__)

timer = Timer(2, 14, 3)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)