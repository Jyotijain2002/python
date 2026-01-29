'''
module:Consider a module to be the same as a code library.A file containing a set of functions you want to include in your application.

to use a module in a file we use import keyword

Note: When using a function from a module, use the syntax: module_name.function_name.

renaming a module: You can create an alias when you import a module, by using the as keyword
'''

import mymodule1 as mm1



mm1.greetings("jyoti")

#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):


print(mm1.person1["name"])
print(mm1.person1)

for keys in mm1.person1.keys():
    print(keys, end=" ")