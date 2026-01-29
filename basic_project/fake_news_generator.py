import random

actions=['jumps','barks','climb','dances','laughs','weeps']

while True:
 welcome=input("hey hii are you ready to create some funny fake news(y/n): ").lower()

 if(welcome=='y'):
    genre=input("choose one of the field for which you wnat to create fake news (sports/bollywood/politics)").lower()

    match genre:
        case "sports":
            player=input("enter you favorite player name")
            action_choose=input('do you want to choose the action(y/n) ')
            action=None
            if(action_choose=='y'):
                action=input("enter an action")
            else:
                action=random.choice(actions)
            place=input("enter one of you favorite place: ")
            
            print(f"{player.capitalize()} {action} near {place}")
        
        case "bollywood":
            actor=input("enter you favorite actor/actress name")
            action_choose=input('do you want to choose the action(y/n) ')
            action=None
            if(action_choose=='y'):
                action=input("enter an action")
            else:
                action=random.choice(actions)
            place=input("enter one of you favorite place: ")
            
            print(f"{actor.capitalize()} {action} near {place}")

        case "politics":
            politician=input("enter you favorite player name")
            action_choose=input('do you want to choose the action(y/n) ')
            action=None
            if(action_choose=='y'):
                action=input("enter an action")
                actions.append(action)
            else:
                action=random.choice(actions)
            place=input("enter one of you favorite place: ")
            
            print(f"{politician.capitalize()} {action} near {place}")
    
 elif welcome=='n':
    print("thanks and bye !!")
    break

 what_next=input("wanna continue(y/n)? ")
 if(what_next=='n'):
     print("thanks for playing , bye bye!!")
     break