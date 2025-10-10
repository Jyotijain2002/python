'''
None: is a special constant that represents the absence of a value
None datatype: NoneType and None is the only instance of NoneType object
'''

x=None
print(x)
print(type(x))

x=4
print(x)

print("false" if None != 0 else print("true"))

res=None
if res is None:
    print("no result yet")
else:
    print("result is ready")

print(None==False)
print(bool(None)) # None evaluates to False in a boolean context.

# function returning None

def myfunc():
    x=5


print(myfunc())

