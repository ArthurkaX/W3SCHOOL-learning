# Write a Python program to print the calendar of a given month and year.
import re
import calendar
while 1:
    year_month = input('Put here year and month in format: YYYY,MM >>>')
    if re.match('[0-9]{4},[0-9]{1,2}',year_month):
        year = int(year_month.split(',')[0])
        month = int(year_month.split(',')[1])
        
        break
    print('wrong input, pls retype...')
cal = calendar.TextCalendar(firstweekday=0)
Mmatrix = cal.monthdayscalendar(year,month)
print(cal.formatmonthname(year,month,10))
print('Monday   Tuesday   Wednesday   Thursday   Friday   Satarday   Sunday', end = '')
for x in Mmatrix:
    print()
    for y in x:
        if (y == 0):
            print('        ', end = '')
        else:
            print(str(y) + '         ', end = '')    


print()
print(Mmatrix)