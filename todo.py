# To-Do List Application

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['name']}")

def add_task(tasks):
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added!")
    else:
        print("Task cannot be empty!")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nThank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
