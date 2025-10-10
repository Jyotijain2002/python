'''
try block: lets you test a block of code for errors

except block: lets you handle the error

else block: lets you execute code when there is no error

finally block: lets you execute code,regardless of the result of try and except blocks

'''

try:
    print(x)
except:
    print('an exception occurred')

try:
    print(x)
except NameError:
    print("variable not defined")
except:
    print("some error has occurred")



# else block: you can use the else keyword to define a block of code to be executed if no errors were raised:

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")


# finally block: The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")
finally:
    print("la la , ha ha , everything is alright")


# try:
#     f=open("text.txt")
#     try:
#       f.write("hahahahhah lljdjhed")
#     except:
#       print("something went wrong while writing in the file")
#     finally:
#       f.close()
# except:
#     print("something went wrong while opening a file")



'''
raise an exception:
to throw(or raise) an exception, use the "raise" keyword
the "raise" keyword is used to raise an exception
you can define what kind of error to raise and text to print to the user
'''


x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
else:
    print(x)

txt = "hello"
if not type(txt) is int:
    raise TypeError("Only integers are allowed")   