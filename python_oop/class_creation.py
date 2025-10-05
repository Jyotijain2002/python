class my_class:
   
   # __init__(): this method is similar to the constructor in cpp it is used to initialize a class variables
   def __init__(self,name,age):
      self.name=name
      self.age=age

# __str__() method: controls what should be return when the class object is represented as a string
# if the __str__() method is not set, the string representation of the object is returned
 
   def __str__(self):
      return f"{self.name},{self.age}"


#creatin method:
   def greetings(self):
    print(f"hello everyone my name is {self.name} and my age is {self.age}")



p1=my_class("jyoti jain",22)
print(p1.name,p1.age)

print(p1) #<__main__.my_class object at 0x000001DEB4825DC0> this the output without using __str__() method
#output with __str__() method:=>  jyoti jain,22

p1.greetings()
