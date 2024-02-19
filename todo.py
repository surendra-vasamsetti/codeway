tasks=[]

def addTask():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def listTasks():
  if not tasks:
    print("There are no tasks currently")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f" Task #{index}. {task}")

def removeTask():
  listTasks()
  try:
    taskToDelete=int(input("Enter the # to Remove:"))
    if taskToDelete >=0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
      
  except:
    print("Invalid input.")


if __name__== '__main__':
  print("Welcome to the To-Do List App")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("___________________________________________")
    print("1.Add a new task")
    print("2.Remove a task")
    print("3.List tasks")
    print("4.Quit")

    choice=input("Enter your choice:-")
    if(choice=='1'):
      addTask()
    elif(choice=='2'):
      removeTask()
    elif(choice=='3'):
      listTasks()
    elif(choice=='4'):
      break
    else:
      print("Invalid choice. Please try again.")

print(" Thank You ,GOODBYE :)")
