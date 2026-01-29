# self paarmeter: is a reference to the current instance of the class, ans is used to access variables that belongs to the class
# it does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.


class person:
    def __init__(my_obj,name,age):
        my_obj.name=name
        my_obj.age=age
    
    def my_function(obj): #obj=self
        print(f"hey hi my name is {obj.name}")


p1=person("jyoti jain",22)
p1.my_function()

# modifying object properties out the class template

p1.age=21
print(p1.age)


# delete object properties using "del keyword"

del p1.age
# print(p1.age) will give error that person oject has no attribute 'age'

#delete object
del p1
# print(p1)  error: name p1 is not defined

del person 
# p1=person("hello",78) # will give error there is no person class 
# print(p1)


#pass statement:
# class definition can not be empty so for some reason you want to have an empty class you can use pass statement

class person:
    pass

p1=person()