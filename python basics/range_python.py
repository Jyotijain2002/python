# range(start,end+1, updation): built-in function returns an immutable sequence of numbers,commonly used for looping a specific number of times

# range with one argument
x=range(10)
print(type(x))
print(list(x))

# range() with two arguments
x=range(1,11)
print(list(x))

# range() with three arguments
x=range(0,11,2)
print(list(x))


# we can do range slicing
print(list(x[2:5]))

#membership testing
if 12 in range(1,34):
    print("is a member")
else:
    print("not a member")


# len() method on range()
print(len(range(3,10)))

