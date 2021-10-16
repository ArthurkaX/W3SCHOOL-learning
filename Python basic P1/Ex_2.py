#  Write a Python program to get the Python version you are using

import sys
import platform

print('Python version is:')
print(sys.version)
print('version info:')
print(sys.version_info)

print()
print(platform.python_version())