
def view_task(tasks):
   if(len(tasks)==0):
     print("Tasks is empty")
   else:
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_all_tasks(tasks):
  name=input("Enter the tasks: ")
  tasks.append(name)


def delete_task(tasks):
  index=int(input("Enter the index: "))
  if 1<=index<=len(tasks):
    del tasks[index-1]
  else:
    print("Invalid choice")
  view_task(tasks)


def main():
   tasks=[]
   while True:
    print("To-d-List Tasks")
    print("1.Addition of the task")
    print("2.Deletion of the task")
    print("3.View of the tasks")
    print("4.Exit the loop")
    choice=input("Enter the choice: ")


    match choice:
      case '1':
        add_all_tasks(tasks)
      case '2':
        delete_task(tasks)
      case '3':
        view_task(tasks)
      case '4':
        break
      case _:
        print("Invalid choice")


if __name__ ==  "__main__":
  main()



       
