tasks =[]
while True:
    print("---- To Do List ----")
    print(" 1. Show task") 
    print(" 2. Add task") 
    print(" 3. Remove task") 
    print(" 4. Exit") 
    choice=int(input("Enter your choice (1-4):"))
    
    if choice == 1 :
        print(" To do list : ")

        i=0
        while i<len(tasks):
            print(str(i+1)+" "+ tasks[i])
            i = i+1
    elif choice == 2 :
        task = input("Enter a task : ")
        tasks.append(task)
        print("Task added")
    elif choice == 3 :
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Current tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == 4 :
        print("Goodbye!")
        break
    else : 
        print("Invalid choice.")