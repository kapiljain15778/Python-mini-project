import random

games=["Stone","Paper","Scissor"]

userscore=0
computerscore=0
rounds=int(input("Enter the number of round"))
while rounds!=0:
 user=input("Enter your choice")
 choice=random.choice(games)
 if(user not in games):
  print("Invalid choice")
  continue
 elif user == choice:
    print("It's a tie!")
 elif(user=="Scissor" and choice=="Paper"):
  userscore+=1

 elif(user=="Stone" and choice=="Scissor"):
  userscore+=1

 elif(user=="Paper" and choice=="Stone"):
  userscore+=1
 else:
  computerscore+=1
 rounds-=1






if userscore > computerscore:
    print("User wins the game!")
elif computerscore > userscore:
    print("Computer wins the game!")
else:
    print("It's a tie overall!")