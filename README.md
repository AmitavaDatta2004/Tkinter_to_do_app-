#  To-Do App

This is a simple Python-based To-Do application with a graphical user interface (GUI) built using `tkinter`. The app allows users to manage tasks by adding, marking them as completed, and viewing both pending and completed tasks. Tasks are saved to a file (`tasks.json`) so that they persist across sessions.

---

## Features

- **Add New Tasks**: Input tasks through the entry field and add them to the pending tasks list.
- **Mark as Complete**: Select a task from the pending list and mark it as completed, moving it to the completed tasks list.
- **Task Persistence**: Tasks are stored in a JSON file (`tasks.json`), ensuring tasks are retained between sessions.
- **User-Friendly GUI**: Easy-to-use interface for managing tasks.

---

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- File system permissions to read/write the `tasks.json` file.

---

## Setup and Usage

1. **Clone the Repository**:  
   Download or clone this code to your local machine.

2. **Run the Script**:  
   Run the script using the following command in your terminal or Python IDE:
   ```bash
   python main.py
   ```

3. **Manage Tasks**:  
   - Enter tasks in the input field and click **Add Task** to add them to the pending list.
   - Select a task in the pending tasks list and click **Complete Task** to mark it as completed.
   - Both pending and completed tasks will be displayed in their respective lists.

4. **Task Persistence**:  
   Tasks are stored in `tasks.json` and automatically loaded when you restart the app.

---

## File Structure

- `main.py`: Main script for the application.
- `tasks.json`: JSON file to store pending and completed tasks (created automatically upon adding tasks).

---

## Code Walkthrough

### Key Functions

1. **load_tasks()**:  
   Reads tasks from `tasks.json`. If the file doesn't exist, initializes an empty task structure.

2. **save_tasks()**:  
   Saves the current state of tasks to `tasks.json`.

3. **add_task()**:  
   Adds a new task to the pending list after validation.

4. **complete_task()**:  
   Moves the selected task from the pending list to the completed list.

5. **refresh_task_list()**:  
   Updates the GUI to display the current list of pending and completed tasks.

---

## GUI Overview

1. **Input Field**:  
   A text box for entering new tasks.

2. **Buttons**:  
   - **Add Task**: Adds the entered task to the pending list.
   - **Complete Task**: Moves a selected task from pending to completed.

3. **Task Lists**:  
   - **Pending Tasks**: Displays tasks yet to be completed.
   - **Completed Tasks**: Displays tasks marked as completed.

---

## Enhancements (Ideas for Future Improvement)

- Add a feature to delete tasks from the lists.
- Provide options to edit tasks.
- Add timestamps for when tasks were added/completed.
- Enhance the GUI with themes and styling.
- Include sorting or filtering options for tasks.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

---

## Author

Amitava Datta