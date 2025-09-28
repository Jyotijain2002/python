#boolean statement gives either True or False value
print(10 > 9) # True
print(10 == 9) #False
print(10 < 9) #False

print(bool("hello")) #True
print(bool(12)) #True
print(bool("")) #False
print(bool())  #False
print(bool(0)) #False
print(bool(1)) #True

'''
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''

#falsy values
print(bool(()))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(0))

