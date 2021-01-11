'''
Exercise 5.1 from thinkpython2

Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

epoch in UNIX systems: 1 January 1970
'''

#by gabrielbarberini

import time

secondsPerMinute = 60
secondsPerHour = secondsPerMinute * 60
secondsPerDay = secondsPerHour * 24

minutesPerDay = secondsPerDay/60
minutesPerHour = secondsPerHour/60

hoursPerDay = minutesPerDay/60

secondsSinceEpoch = time.time()
daysSinceEpoch = secondsSinceEpoch // secondsPerDay
hoursSinceEpoch = secondsSinceEpoch // secondsPerHour
minutesSinceEpoch = secondsSinceEpoch // secondsPerMinute

hoursNow = hoursSinceEpoch % hoursPerDay
minutesNow = (minutesSinceEpoch % minutesPerDay) % minutesPerHour
secondsNow = (secondsSinceEpoch % secondsPerDay) % secondsPerMinute

timeNow = str(int(hoursNow)) + ":" + str(int(minutesNow)) + ":" + str(int(secondsNow))

print("\n\nNow HH:MM/SS (UTC):", timeNow)
print("Days since epoch:", daysSinceEpoch, "\n\n")


