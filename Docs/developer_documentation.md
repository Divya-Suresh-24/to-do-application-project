# Developer's Documentation for Prioritized To-Do List App

---

## Overview

The **Prioritized To-Do List App** is a task management application designed to simplify personal and professional responsibilities. Users can create tasks, assign priority levels (High, Medium, Low), categorize tasks (Work, Personal, School), and set due dates with optional notifications.

This document provides detailed insights for developers to understand, extend, and maintain the project.

---

## Implementation Overview

### Implemented Features
1. **Task Management**: Add, edit, complete, and delete tasks.
2. **Categorization and Prioritization**: Organize tasks by categories and priority levels.
3. **Filtering**: Filter tasks by priority, due date, or category.
4. **Task History**: View completed tasks.
5. **Session State**: Temporarily store tasks during the session using `st.session_state`.

### Unimplemented Features
1. **Persistent Storage**: No database integration; tasks are session-based.
2. **Notifications**: No reminders for due dates implemented yet.

---

## Installation, Deployment, and Admin Guide

### Assumptions
- The app is already installed as per the User Guide.
- Python 3.8 or higher is installed.

### Additional Setup
- For local deployment, no further setup is required beyond dependencies listed in `requirements.txt`.
- If deploying on **Streamlit Cloud**:
  1. Push the repository to GitHub.
  2. Link the repository to Streamlit Cloud for hosting.

---

## User Interaction and Code Walkthrough

### User Flow Recap
1. **Home Screen**: Users create tasks and view pending/completed tasks.
2. **Filtering**: Sidebar allows users to filter tasks.
3. **History Tab**: View completed tasks for productivity tracking.

### Code Walkthrough
#### Key Modules and Functions
- **`app.py`**:
  - Entry point for the application.
  - Manages user interaction via Streamlit widgets.
  - Handles session state for task management.

- **Task Management Functions**:
  - `add_task(task: str, priority: str, category: str, due_date: datetime)`:
    Adds a task to the session state.
  - `delete_task(task_id: int)`:
    Deletes a task based on its ID.
  - `filter_tasks(criteria: dict)`:
    Filters tasks by user-defined criteria.

#### Code Flow
1. **Startup**:
   - `streamlit run app.py` initializes the app.
   - The `app.py` script sets up the Streamlit interface.

2. **Task Actions**:
   - Adding a task updates `st.session_state['tasks']`.
   - Filtering applies criteria to `st.session_state['tasks']`.

3. **Task History**:
   - Completed tasks are moved to `st.session_state['completed_tasks']`.

---

## Known Issues

### Minor
1. **Session Reset**:
   - Tasks are lost upon refreshing the page.
   - **Solution**: Add database or file-based storage.

2. **Filtering Edge Cases**:
   - Incorrect combinations of filters may show no results.
   - **Solution**: Validate filter criteria in the UI.

### Major
1. **No Persistent Storage**:
   - Users lose all data after the session ends.
   - **Solution**: Integrate SQLite or cloud storage like Firebase.

---

## Future Work

### Enhancements
1. **Storage**:
   - Add persistent storage with SQLite or Firebase.
2. **Notifications**:
   - Integrate notification systems (e.g., email or mobile alerts).
3. **Improved Filtering**:
   - Allow multi-criteria sorting and advanced search capabilities.
4. **UI Enhancements**:
   - Add custom themes and better mobile responsiveness.

---

## Known Computational Inefficiencies

1. **Large Task Lists**:
   - Current implementation relies on in-memory operations, which may slow down with large datasets.
   - **Solution**: Optimize task filtering with a database query-based approach.

2. **Date Handling**:
   - Date comparisons are done in pure Python, which can be inefficient.
   - **Solution**: Use libraries like `numpy` for batch date processing.

---

## Graphics and Diagrams

### Task Flow Diagram
```plaintext
User Action ---> app.py (Streamlit Interface) ---> Task Management Functions ---> Session State
```
### Class Diagram
+------------------+
|    Task          |
+------------------+
| - id: int        |
| - name: string   |
| - priority: str  |
| - category: str  |
| - due_date: str  |
+------------------+
         ^
         |
+-------------------------+
| TaskManager             |
+-------------------------+
| - tasks: list           |
+-------------------------+
| + add_task()            |
| + delete_task()         |
| + filter_tasks()        |
| + modify_tasks()        |
| + view_completed_tasks()|
| + mark_completed()      |
| + mark_as_pending()     |
+-------------------------+

### State Diagram
+------------------+    Mark as Completed     +--------------------+
|    Pending       | -----------------------> |    Completed       |
+------------------+                           +--------------------+
       ^                                            |
       |                                            |
Delete Task                                      Archive Task
       |                                            |
+------------------+                           +--------------------+
|   Deleted        | <----------------------- |    Archived        |
+------------------+                           +--------------------+

### Screenshot of the app

![App Screenshot](assets/todoapp.png)


---
# Ongoing Development and Maintenance

---

## Suggestions for Future Developers

### Unit Testing
- Add unit tests for key task management functions such as `add_task()`, `delete_task()`, and `filter_tasks()`. This will ensure that the app functions correctly and remains reliable as new features are added or existing code is modified.

### Subclassing
- Consider using object-oriented programming (OOP) to structure the code more efficiently. This would involve creating classes for `Task`, `Category`, and `Filter` to manage and manipulate tasks, categories, and filters. Subclassing could also be used to extend the functionality of the app in the future.

### Documentation
- Regularly update this **Developer's Guide** and the **README.md** files with any major updates, new features, or significant changes to the project. Clear and up-to-date documentation ensures that future developers can easily understand the code and contribute to the project.

---

## File Structure

```
|- app.py           # Main Streamlit app
|- requirements.txt # List of dependencies
|- README.md        # User guide and project documentation
|- tasks.csv           # holds pending task data
|- completed_tasks.csv         # holds completed task data
```


---

## Notes

- This guide is a living document. Updates should be made as the project evolves. Reach out to the project maintainer for further clarification or support.
