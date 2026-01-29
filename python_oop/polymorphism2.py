class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("move")

class car(vehicle):
 pass

class boat(vehicle):
   def move(self):
      print("sail")

class plane(vehicle):
   def move(self):
      print("fly")

car1=car('huwei',"sonet")
boat1=boat("ibiza","natty-20")
plane1=plane("air_india","boeing-717")

for x in (car1,boat1,plane1):
   print(x.brand)
   print(x.model)
   x.move()

'''
In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
Because of polymorphism we can execute the same method for all classes.
'''