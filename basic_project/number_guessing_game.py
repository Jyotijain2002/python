import random

random_num=random.randint(1,100)

while True:
    try:
       
       num=int(input("take a guess (1-100) "))
       if num<0 and num>100:
        print('Enter number in range (1-100)')
       elif num < random_num:
        print("your guess is too low")
       elif num>random_num:
        print("your guess is too high")
       elif num==random_num:
        print("congratulations you win the game!! ")
        break
       
    except ValueError:
        
        print("please enter a valid number")
       