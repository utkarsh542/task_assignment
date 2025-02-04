import json
import os
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file or return an empty list if the file does not exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, deadline, priority="medium"):
    """Add a new task to the JSON file."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "status": "pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("\nTask added successfully!")

def view_tasks(filter_by=None, sort_by=None):
    """View all tasks or filter by status (pending/completed) and sort by deadline or priority."""
    tasks = load_tasks()
    if filter_by:
        tasks = [task for task in tasks if task["status"] == filter_by]
    if sort_by == "deadline":
        tasks.sort(key=lambda x: x["deadline"] or "9999-12-31")
    elif sort_by == "priority":
        priority_order = {"high": 1, "medium": 2, "low": 3}
        tasks.sort(key=lambda x: priority_order.get(x.get("priority", "medium"), 2))

    if tasks:
        print("\nTask List:")
        for task in tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | "
                  f"Deadline: {task['deadline'] or 'N/A'} | "
                  f"Priority: {task.get('priority', 'medium')} | "
                  f"Status: {task['status']}")
    else:
        print("\nNo tasks found.")


def update_task(task_id, new_description=None, new_status=None, new_priority=None):
    """Update a task's description, status, or priority."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if new_description:
                task["description"] = new_description
            if new_status:
                task["status"] = new_status
            if new_priority:
                task["priority"] = new_priority
            save_tasks(tasks)
            print("\nTask updated successfully!")
            return
    print("\nTask ID not found!")

def delete_task(task_id):
    """Delete a task from the JSON file."""
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) < len(tasks):
        save_tasks(updated_tasks)
        print("\nTask deleted successfully!")
    else:
        print("\nTask ID not found!")

def search_task(keyword):
    """Search tasks by description."""
    tasks = load_tasks()
    found_tasks = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if found_tasks:
        print("\nSearch Results:")
        for task in found_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Deadline: {task['deadline']} | Priority: {task['priority']} | Status: {task['status']}")
    else:
        print("\nNo matching tasks found.")

def due_soon():
    """Notify users about tasks that are due within 24 hours."""
    tasks = load_tasks()
    now = datetime.now()
    soon_tasks = [task for task in tasks if task["deadline"] and datetime.strptime(task["deadline"], "%Y-%m-%d") <= now + timedelta(days=1)]
    if soon_tasks:
        print("\nTasks Due Soon:")
        for task in soon_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Deadline: {task['deadline']} | Status: {task['status']}")
    else:
        print("\nNo urgent tasks.")

def menu():
    """Display the CLI menu."""
    while True:
        print("\nTask Management System")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. View Pending Tasks")
        print("4. View Completed Tasks")
        print("5. Update a Task")
        print("6. Delete a Task")
        print("7. Search Tasks")
        print("8. View Tasks Due Soon")
        print("9. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD) or press Enter to skip: ") or None
            priority = input("Enter priority (high/medium/low): ") or "medium"
            add_task(desc, deadline, priority)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks(filter_by="pending")

        elif choice == "4":
            view_tasks(filter_by="completed")

        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_desc = input("Enter new description (leave empty to keep unchanged): ")
                new_status = input("Enter new status (pending/completed, leave empty to keep unchanged): ")
                new_priority = input("Enter new priority (high/medium/low, leave empty to keep unchanged): ")
                update_task(task_id, new_desc if new_desc else None, new_status if new_status else None, new_priority if new_priority else None)
            except ValueError:
                print("\nInvalid input. Please enter a valid task ID.")

        elif choice == "6":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("\nInvalid input. Please enter a valid task ID.")

        elif choice == "7":
            keyword = input("Enter keyword to search: ")
            search_task(keyword)

        elif choice == "8":
            due_soon()

        elif choice == "9":
            print("\nExiting Task Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    menu()
