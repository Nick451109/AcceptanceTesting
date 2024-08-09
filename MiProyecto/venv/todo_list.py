class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = task["status"]
                print(f"{index}. {task['task']} - {status}")
        return self.tasks  # Asegúrate de devolver la lista de tareas

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Completed"
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

def print_menu():
    print("\nTo-Do List Manager")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Clear the entire to-do list")
    print("6. Exit")

def main():
    todo_list = ToDoList()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            todo_list.list_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == "4":
            todo_list.list_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ")
            if confirm.lower() == 'y':
                todo_list.clear_tasks()
        elif choice == "6":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
