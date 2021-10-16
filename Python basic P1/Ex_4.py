# Write a Python program to display the current date and time

import math, re
print('Простой калькулятор площади окружности.')
while 1:
    R = input('введите радиус >>>')
    if re.match('[0-9]{1,255}', R):
        break
    print('Введите снова')

print('площадь равна:')
print(math.pi * float(R) ** 2)