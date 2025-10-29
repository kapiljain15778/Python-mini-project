
import random

freq={}
def roll_once():
  num=random.randint(1,6)
  freq[num]=freq.get(num,0)+1
  print(num)
  print(freq)


def roll_multiple_time():
  num=int(input("Enter the number"))
  result=[]
  for _ in range(num):
    ans=random.randint(1,6)
    result.append(ans)
    freq[ans]=freq.get(ans,0)+1
  print(result)

def freq_all():
    print(freq)

def main():
  while True:
    print("Die Rolling Game")
    print("1.Want to roll die once only")
    print("2.Want to roll die multiple times")
    print("3.To Get the frequency of all numbers")
    print("4.Exit the loop")
    choice=input("Enter the number")
    if choice=='1':
      roll_once()
    elif choice=='2':
      roll_multiple_time()
    elif choice=='3':
      freq_all()
    elif choice == '4':
      print("Exiting... Goodbye! 🎲")
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  main()