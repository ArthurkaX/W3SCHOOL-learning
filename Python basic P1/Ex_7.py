# Write a Python program to accept a filename from the user and print the extension of that.

file_name = input('write the name of file, including extension >>> ')

if file_name.find('.') == -1:
    print('your file name does\'t have an extension')
    quit()
if file_name.find('.') >= len(file_name) - 1:
    print('your file name have empty extension') 
    quit()

print('Extension of file name is: ' + file_name[file_name.find('.')+1:])

print('get by splitting: ' + file_name.split('.')[-1])