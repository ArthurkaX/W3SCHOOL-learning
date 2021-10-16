# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
import pydoc
func = input('enter name of function >>>')
strhelp = pydoc.render_doc(func, "Help on %s")
print(strhelp)

print(abs.__doc__)