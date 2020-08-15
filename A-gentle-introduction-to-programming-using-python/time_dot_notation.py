"""As an exercise, write a function called print_time that takes a Time object and prints it in the form hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least two digits, including a leading zero if necessary.
Write a boolean function called is_after that takes two Time objects, t1 and t2, and re- turns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement."""

class Time:
    hour = 3
    minute = 34
    second = 51 

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

time = Time()
print_time(time)
