import random
secret_number = random.randint(1, 10)
guess=0

while True:
  choice=int(input("Enter the number"))
  if(choice==secret_number):
    print("Yes the number matched after number of guesses: ", guess)
    break
  else:
    guess+=1
