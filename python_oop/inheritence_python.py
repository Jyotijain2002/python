# inheritence: allows us to define a class that inherits all the methods and properties from another class
# creating a parent class

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_name(self):
        print(f"my name is {self.name}")


#creating child class
class student(person): # person->parent class , student->child class

# the child class __init__() function overrides the inheritence of the parent class __init__() function

# to keep the inheritence of parent's __init__() function, add a call to parent's __init__() function
    # def __init__(self, name,age):
    #     person.__init__(self, name,age)
          

# use of super keyword: the super() function is used to give access to methods and properties of a parent or sibling class
# the super() function returns an object that represent the parent class
#super() function dont take any parameters

    def __init__(self,name,age):
        super().__init__(name,age)

    # def __str__(self): # this method returns not print
    #     return f"{self.standard},{self.rno}"

p1=person("jyoti",12)
p1.print_name()

s1=student("hello",23)
s1.print_name()



class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greeting(self):
        print(f"hello my name is {self.name}")

class doctor(human):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.occupation="doctor"
        self.education="phd"
        

    
    def __str__(self):
        return f"{self.name},{self.age},{self.education},{self.occupation}"
    
person1=human("jj","34")

h1=doctor("jyoti",28)
print(h1)