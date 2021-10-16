# Write a Python program to display the current date and time

import datetime

print('first variant:')
print('current date & time is:')
print(datetime.datetime.now())

now = datetime.datetime.now

print('second variant:')
print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
