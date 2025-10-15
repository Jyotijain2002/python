import random

def dice_roll():
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    print(f"({num1},{num2})")


while True:
    choice=input("wanna roll the dice (y/n) ").lower()
    if choice=='y':
        dice_roll()
    elif choice=='n':
        print('thanks for playing, bye bye')
        break
    else:
        print("Invalid,enter a correct choice")

