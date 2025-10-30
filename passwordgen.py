import random
import string


length=int(input("Enter the length of the password: "))
if(length<7):
  print("⚠️ Password too short! Please use at least 8 characters for better security.")

else:
 all_chars=string.ascii_letters + string.digits + string.punctuation
 password=""
 for _ in range(length):
   password+=random.choice(all_chars)

 print("The final random password is : ", password)

#  string.ascii_letters + string.digits + string.punctuation -> Not aware of this methods 