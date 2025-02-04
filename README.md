## Task Management System

### Overview
This is a simple **Command Line Interface (CLI) Task Management System** that allows users to efficiently manage their tasks by adding, viewing, updating, deleting, searching, and prioritizing them. The system also provides due date reminders for tasks that are approaching their deadlines.

## How to Run the Program

### Ensure Python is Installed
- You need **Python 3.x** installed on your system. You can check your Python version using:
  ```sh
  python --version
  ```

### Download the Script
- Clone the repository or download the script file (`task_manager.py`).

### Run the Program
- Open a terminal or command prompt and navigate to the script directory.
- Execute the following command:
  ```sh
  python task_manager.py
  ```

### Follow On-Screen Instructions
- The CLI menu will guide you through managing tasks.

## Features

### Core Features
✅ **Add Tasks** - Create a new task with a description, deadline, and priority (high/medium/low).
✅ **View Tasks** - View all tasks, pending/completed tasks, and sort by deadline or priority.
✅ **Update Tasks** - Modify a task’s description, status, or priority level.
✅ **Delete Tasks** - Permanently remove a task.
✅ **Search Tasks** - Find tasks by keyword in the description.
✅ **Due Date Reminders** - Alerts for tasks due within 24 hours.

### Additional Features
✅ **Task Prioritization** - Tasks can have **high, medium, or low** priority.
✅ **Sorting** - Sort tasks by **deadline** or **priority** for better organization.

## Design Decisions & Assumptions
- **Data Storage**: All tasks are stored in `tasks.json` to persist data between sessions.
- **Sorting & Filtering**: Tasks can be filtered by **status** and sorted by **deadline or priority**.
- **Date Format**: The system accepts deadlines in `YYYY-MM-DD` format.
- **CLI Interface**: A simple text-based interface for lightweight usability.



