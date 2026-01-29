# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# i python function is created using def keyword

def greetings(name):
    print(f"hello,{name}")

name="jyoti"
greetings(name)

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a "tuple" of arguments, and can access the items accordingly:

def sum(*args):
    s=0
    for num in args:
        s+=num
    return s

print(sum(34,23,56,987,1024))

# keyword arguments
def merit(num1, num2):
    return num1+num2
print(merit(num1=23,num2=78))

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def func(**kargs):
    for num in kargs.values():
        print(num)

func(num1=1,num2=2,num3=3,num4=4)


#default parameter
def my_func(name="jyoti jain"):
    print(name)

my_func("harshita")

#positional-only arguments
# specify that a function can have only positional arguments, add 
# , /
# after the arguments:
#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
#But when adding the , / you will get an error if you try to send a keyword argument:

def my_function(x,y,z,/):
    return x+y+z
#print(my_function(x=2,y=3,z=4)) #it will give array beacuse we can only give positional argument but we are giving keyword argument

print(my_function(4,7,9))

# similar we can use 
# *,
#  before the arguments for passing only keyword argumenets

def my_f(*,x,y,z):
    return x*y*z 
#print(my_f(3,2,1)) will give error for using postional arguments instead keyword arguments 
print(my_f(x=3,y=2,z=1))
