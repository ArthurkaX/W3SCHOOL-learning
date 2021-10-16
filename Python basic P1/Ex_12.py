# Write a Python program to print the calendar of a given month and year.

import calendar
input('Put here year and month in format: YYYY,MM >>>')
cal = calendar.TextCalendar(firstweekday=0)

for i in cal.itermonthdays(2021,10):
    print(i)

print(cal.monthdayscalendar(2021,10))