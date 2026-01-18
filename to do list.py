def task():
   tasks=[]
   print("A TO-DO LIST")
   total_task=int(input("Enter the total number of tasks: "))
   for i in range(1,total_task+1):
       task_name=input(f"Enter the task name{i}: ")
       tasks.append(task_name)
   print(f"Today's tasks are:{tasks}")
   while True:
       print("\nChoose an operation:")
       print("1 -> ADD")
       print("2 -> UPDATE")
       print("3 -> DELETE")
       print("4 -> VIEW")
       print("5 -> EXIT")
       try:
           operation = int(input("Enter your choice: "))
       except ValueError:
           print("Invalid input. Enter a number between 1 and 5.")
           continue
       if operation==1:
           add=input("Enter the task name: ")
           tasks.append(add)
           print(f"Task {add} added successfully")

       elif operation == 2:
           update_val = input("Enter task name to update: ").strip()
           if update_val in tasks:
               up = input("Enter new task name: ").strip()
               index = tasks.index(update_val)
               tasks[index] = up
               print(f"Task '{update_val}' updated to '{up}'.")
           else:
               print("Task not found.")

       elif operation==3:
           delete_val=input("Enter the task name to del: ")
           if delete_val in tasks:
               ind=tasks.index(delete_val)
               del tasks[ind]
               print(f"Task {delete_val} deleted successfully")

       elif operation==4:
           if tasks:
               print("\nYour Tasks:")
               for i, t in enumerate(tasks, start=1):
                   print(f"{i}. {t}")
           else:
               print("No tasks available.")

       elif operation==5:
           print("exit prgrm")
           break
       else:
            print("invalid input")
if __name__=="__main__":
    task()

