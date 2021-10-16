# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

number_sequence = input('enter some number diveded by comma >>>')
# checking

# make list
l1 = []
num = ''
for x in number_sequence:
    if x != ',':
        num = num + x
    else:
        l1.append(num)
        num = ''
print('list:', end = '')
print(l1)

# make tuple
t1 = ()
num = ''
for x in number_sequence:
    if x == ',':
        num = ''        
    else:
        num = num + x
        t1 = t1 + tuple(num)
        
print('tuple:', end = '')
print(t1)