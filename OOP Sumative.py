# task_manager.py

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True
        print(f"Task '{self.title}' marked as complete.")

    def display(self):
        status = "Done" if self.completed else "Pending"
        print(f"Task: {self.title}\nDescription: {self.description}\nStatus: {status}\n")


# Inherits from Task
class UrgentTask(Task):
    def __init__(self, title, description, due_date):
        super().__init__(title, description)
        self.due_date = due_date

    def display(self):
        status = "Done" if self.completed else "Pending"
        print(f"URGENT Task: {self.title}\nDescription: {self.description}\nDue: {self.due_date}\nStatus: {status}\n")

    def is_overdue(self, current_date):
        return current_date > self.due_date


# Demo usage
if __name__ == "__main__":
    task1 = Task("Grocery Shopping", "Buy milk, eggs, and bread.")
    task2 = UrgentTask("Project Deadline", "Finish the project report.", "2025-06-05")

    task1.display()
    task2.display()

    task1.mark_complete()
    task2.mark_complete()

    task1.display()
    task2.display()

    # Check if the urgent task is overdue
    current_date = "2025-06-10"
    if task2.is_overdue(current_date):
        print(f"The task '{task2.title}' is overdue!\n")