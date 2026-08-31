# Mini-Project: Personal Task Manager
# A command-line To-Do/Task Manager that saves all tasks inside a tasks.json file

import json

class TO_DO():
    
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("Personal Task Manager Project\\task.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("Personal Task Manager Project\\task.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self):
        task = input("Enter a new task: ")
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['task']}")

    def complete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                if 0 <= index < len(self.tasks):
                    self.tasks[index]["completed"] = True
                    self.save_tasks()
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= index < len(self.tasks):
                    del self.tasks[index]
                    self.save_tasks()
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")