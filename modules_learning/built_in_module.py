import platform as p

x=p.system()
print(x)
x=p.architecture()
print(x)
x=p.machine()
print(x)
x=p.node()
print(x)
x=p.platform()
print(x)
x=p.processor()
print(x)
x=p.uname()
print(x)
x=p.python_compiler()
print(x)
x=p.mac_ver()
print(x)
x=p.java_ver()
print(x)


# dir() function: is a bilt-in function to list all function names or 
# variables in a module.
'''
syntax: dir(module_name)
'''
# x=dir(p)
# print(x,end='\n')

x=p.version()
print(x)