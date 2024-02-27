def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Display Tasks")
    print("4. Exit")

def add_task(todo_dict):
    task = input("Enter the task: ")
    todo_dict[task] = False
    print(f"Task '{task}' added to the to-do list.")

def mark_completed(todo_dict):
    task = input("Enter the task to mark as completed: ")
    if task in todo_dict:
        todo_dict[task] = True
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def display_tasks(todo_dict):
    if todo_dict:
        print("\nTo-Do List:")
        for task, completed in todo_dict.items():
            status = "Completed" if completed else "Not Completed"
            print(f"{task}: {status}")
    else:
        print("\nTo-Do List is empty.")

def todo_list():
    todo_dict = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task(todo_dict)
        elif choice == '2':
            mark_completed(todo_dict)
        elif choice == '3':
            display_tasks(todo_dict)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    todo_list()
