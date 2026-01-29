# decorator let you add extra behavior to a function, without changing the function's. A decorator is a function that takes another function as input and returns a new function.

# basic decorator: define the decorator first, then apply it with 
#  @decorator_name above the function


def change_case(func):
    def inner_func():
        return func().upper()
    return inner_func

@change_case
def myfunction():
    return "hello to world from jyoti"

print(myfunction())

#a decorator can be called multiple times