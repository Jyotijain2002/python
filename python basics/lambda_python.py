# lambda function is small anonymous function, that can take any number of arguments, but can only have one expression.

# syntax:=  lambda arguments:expression

lam_func=lambda x,y,z :x+y+z
print(lam_func(2,5,6))


# use of lambda: power of lambda is better shown when you use them as anonymous function inside another function

def myfunc(n):
    return lambda a:a*n
my_lam_func=myfunc(2)
print(my_lam_func(12))