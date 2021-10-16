# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

number = int(input('Enter a integer number >>> '))

print(number + int('%s%s'%(number,number)) + int('%s%s%s'%(number,number,number)))