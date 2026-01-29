'''
scope: A variable is only available from inside the region it is created. This is called scope.
scopes: 1) local scope  2) global scope

global keyword: If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.
'''

def my_func():
    i=0 #local variable
    while i<=10:
        print(i)
        i+=2

my_func()
#print(i) will give error i undefined

a=0
def func():
    global a
    while a <=10:
        print(a)
        a+=2
print(a)
func()

'''
You're correct that a is defined globally, so it is accessible for reading inside the function. However, when you use a += 2 (which is equivalent to a = a + 2), Python interprets this as an assignment to a local variable a within the function's scope. Once Python sees an assignment to a inside func(), it treats a as local for the entire function, even before the assignment. Therefore, when print(a) is executed before the local a is defined, Python raises an UnboundLocalError because you're trying to read a local variable before it's initialized.

To modify a global variable inside a function, you must explicitly declare it as global using global a at the beginning of the function.

You're absolutely right that a is defined globally and should be accessible. However, in Python, reading a global variable inside a function works without any special declaration, but modifying it (like with a += 2) triggers a different behavior.

When Python sees an assignment to a variable inside a function (even an augmented assignment like +=), it assumes that variable is local to that function unless told otherwise. So when the function tries to execute print(a) before a += 2, it's looking for a local a that hasn't been initialized yet, hence the UnboundLocalError.

To fix this, you must explicitly tell Python to treat a as global within the function using the global keyword:
'''


# nonlocal keyword: is used to work with variables inside nested functions
# the nolocal keyword makes the variable belong to the outer function


def my_func1():
    x="jyoti"
    def my_func2():
        nonlocal x # if we don't use nonlocal keyword then it will return x as "jyoti instead jj because x become local for my_func2() so changes will only limited to my_func2()"
        x="jj"
    my_func2()
    return x

print(my_func1())