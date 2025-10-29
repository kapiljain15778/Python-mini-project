a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
choice=int(input("Enter the choice: "))
if(choice==1):
  print("Perform addition")
  sum=a+b
  print(sum)
elif(choice==2):
  print("Perform Subtraction")
  if(a>b):
    sub=a-b
  else:
    sub=b-a
  print(sub)
elif(choice==3):
  print("Perform Multiply")
  pro=a*b
  print(pro)
elif(choice==4):
  print("Perform division")
  if(a>b):
    div=a/b
  else:
    div=b/a
  print(div)
else:
  print("Invalid choice")
  exit