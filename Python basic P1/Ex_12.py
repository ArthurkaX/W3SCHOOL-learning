# Write a Python program to print the calendar of a given month and year.
import re
import calendar
while 1:
    year_month = input('Put here year and month in format: YYYY,MM >>>')
    if re.match('[0-9]{4},[0-9]{1,2}',year_month):
        year = int(year_month.split(',')[0])
        month = int(year_month.split(',')[1])
        if month > 12 or month <1:
            print('month should be 1 - 12')
        else:    
            break
    print('wrong input, pls retype...')
cal = calendar.TextCalendar(firstweekday=0)
daynames = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
dates = cal.monthdayscalendar(year,month)

print(cal.formatmonthname(year,month,10))

for x in daynames:
    print(x, end='\t')

for x in dates:
    print()
    for y in x:
        if (y != 0):
            print(y, end='')
        print('\t', end='')
        


#print(cal.itermonthdays20(year,month))
#cal.pryear(year, w=2, l=1, c=6, m=3)

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))