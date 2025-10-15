import random

dict1={
 "r":'🪨',
 "p":'📃',
 "s":'✂️'
}
choices=('r','p','s')

while True:
 user=input("rock, paper or scissor? (r/p/s) ").lower()
 if user not in ('r','p','s'):
  print('enter correct choice from r/p/s')
  continue
 
 computer_choice=random.choice(choices)
 
 print(f"user choice: {dict1[user]}")
 print(f"computer choice: {dict1[computer_choice]}")

 if user==computer_choice:
  print("tie!!")
 elif (user=='r' and computer_choice=='s') or (user=='p' and computer_choice=='r') or (user=='s' and computer_choice=='p'):
  print("you won!!")
 else:
  print("you loss!!")
 
 next=input("wnat to continue? (y/n): ").lower()
 if(next=='n'):
  print("thanks for playing!!!!")
  break
 

 # modularise your code in a clear and readable way using function 