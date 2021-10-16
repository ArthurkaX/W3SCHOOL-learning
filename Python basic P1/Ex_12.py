# Write a Python program to print the calendar of a given month and year.
import re
import calendar
while 1:
    year_month = input('Put here year and month in format: YYYY,MM >>>')
    if re.match('[0-9]{4},[0-9]{2}',year_month):
        break
    print('wrong input, pls retype...')
cal = calendar.TextCalendar(firstweekday=0)

for i in cal.itermonthdays(2021,10):
    print(i)

print(cal.monthdayscalendar(2021,10))