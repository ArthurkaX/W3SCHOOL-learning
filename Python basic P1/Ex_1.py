# Write a Python program to print the following string in a specific format

some_txt = 'Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are'


x = 0
for a in some_txt:
    if a.isupper() == True and a != 'I':
        print()
    if a == 'H': 
        x = 1
    if a== 'U' or a== 'L': 
        x = 2

    for tab in range(x):
        print('\t' , end = '')
    x = 0    
  
    print(a, end = '')