class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                if "✓" in task:
                    print(f"{i+1}. {task}")
                else:
                    print(f"{i+1}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if index < 0 or index >= len(self.tasks):
                    print("Invalid task number.")
                else:
                    del self.tasks[index]
                    print("Task deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def mark_task(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                if index < 0 or index >= len(self.tasks):
                    print("Invalid task number.")
                else:
                    task = self.tasks[index]
                    if "✓" in task:
                        self.tasks[index] = task.replace("✓", "")
                        print("Task marked as incomplete.")
                    else:
                        self.tasks[index] = f"{task} ✓"
                        print("Task marked as complete.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add a task")
            print("2. View all tasks")
            print("3. Delete a task")
            print("4. Mark a task as complete")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.delete_task()
                elif choice == 4:
                    self.mark_task()
                elif choice == 5:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a choice.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()