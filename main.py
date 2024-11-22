import tkinter as tk
from tkinter import messagebox
import json

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pending": [], "completed": []}

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks["pending"].append(task)
        task_entry.delete(0, tk.END)
        refresh_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Mark a task as complete
def complete_task():
    selected_task = pending_listbox.curselection()
    if selected_task:
        task = pending_listbox.get(selected_task)
        tasks["pending"].remove(task)
        tasks["completed"].append(task)
        refresh_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete!")

# Refresh the task list display
def refresh_task_list():
    pending_listbox.delete(0, tk.END)
    completed_listbox.delete(0, tk.END)
    for task in tasks["pending"]:
        pending_listbox.insert(tk.END, task)
    for task in tasks["completed"]:
        completed_listbox.insert(tk.END, task)

# GUI Setup
app = tk.Tk()
app.title("Linear Algebra To-Do App")
app.geometry("500x400")

# Input Field
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Pending Tasks Label and Listbox
pending_label = tk.Label(app, text="Pending Tasks:")
pending_label.pack(pady=5)
pending_listbox = tk.Listbox(app, height=10, width=50)
pending_listbox.pack(pady=5)

# Complete Task Button
complete_button = tk.Button(app, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

# Completed Tasks Label and Listbox
completed_label = tk.Label(app, text="Completed Tasks:")
completed_label.pack(pady=5)
completed_listbox = tk.Listbox(app, height=10, width=50)
completed_listbox.pack(pady=5)

# Load tasks and refresh display
tasks = load_tasks()
refresh_task_list()

# Start the application
app.mainloop()
