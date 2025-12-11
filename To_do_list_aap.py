# CODSOFT - TASK 1: TO-DO LIST APP

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        index = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[index - 1] = new_task
        print("Task updated!")
    except:
        print("Invalid selection!")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        tasks.pop(index - 1)
        print("Task deleted!")
    except:
        print("Invalid selection!")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")
