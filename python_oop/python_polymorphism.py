'''
polymorphism = many forms
eg:
in string len() gives the length of the string
in list, len() gives the number of items in the list
similarly in tuple and dictionary


class polymorphism:
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
'''

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive !!!")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model 
   
    def move(self):
        print("Sail !!!")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model 
   
    def move(self):
        print("Fly !!!")


c1=Car("tata","nexon")
b1=Boat("ibiza","netty-20")
p1=Plane("air-india","boeing-771")

for  x in (c1,b1,p1):
    x.move() # due to polymorphism we can execute the same method for all three classes

        


