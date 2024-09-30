# -*- coding: utf-8 -*-
"""main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tRnGh5fq7DpjdFMm74G4AIIDLPfsH5Jc
"""

import csv
from datetime import datetime

# Define the CSV file path
CSV_FILE = '/content/tasks.csv'

# Initialize CSV with headers if it doesn't exist
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'category', 'priority', 'deadline', 'status'])
    except FileExistsError:
        pass  # CSV already exists

def add_task():
    title = input("Enter task title: ")

    # Category input
    category = input("Enter category (Work, Personal, School): ").strip().capitalize()
    while category not in ['Work', 'Personal', 'School']:
        category = input("Invalid category. Please enter Work, Personal, or School: ").strip().capitalize()

    # Priority input
    priority = input("Enter priority (High, Medium, Low): ").strip().capitalize()
    while priority not in ['High', 'Medium', 'Low']:
        priority = input("Invalid priority. Please enter High, Medium, or Low: ").strip().capitalize()

    # Deadline input
    add_date = input("Do you want to add a deadline? (y/n): ").strip().lower()
    if add_date == 'y':
        deadline = input("Enter deadline (YYYY-MM-DD HH:MM): ")
        try:
            datetime.strptime(deadline, '%Y-%m-%d %H:%M')  # Validate date format
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
            return
    else:
        deadline = "None"

    status = "Not Done"

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, category, priority, deadline, status])
    print("Task added successfully!")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("Current Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. Title: {task.get('title', 'N/A')}, "
              f"Category: {task.get('category', 'N/A')}, "
              f"Priority: {task.get('priority', 'N/A')}, "
              f"Deadline: {task.get('deadline', 'N/A')}, "
              f"Status: {task.get('status', 'N/A')}")
    print()  # Extra newline for better readability

def read_tasks():
    tasks = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Read task:", row)
            tasks.append(row)
    return tasks

def delete_task():
    tasks = read_tasks()
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks()  # Show tasks before deletion
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    confirmation = input(f"Are you sure you want to delete '{tasks[task_index]['title']}'? (y/n): ")
    if confirmation.lower() == 'y':
        tasks.pop(task_index)
        rewrite_csv(tasks)
        print("Task deleted successfully.")
    else:
        print("Deletion canceled.")

def rewrite_csv(tasks):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'category', 'priority', 'deadline', 'status'])  # Write header
        for task in tasks:
            writer.writerow([task['title'], task['category'], task['priority'], task['deadline'], task['status']])

def modify_task():
    # Placeholder for modifying tasks
    print("Modify task functionality is not implemented yet.")

def mark_task_done():
    # Placeholder for marking tasks as done
    print("Mark task as done functionality is not implemented yet.")

def filter_tasks():
    # Placeholder for filtering tasks
    print("Filter tasks functionality is not implemented yet.")

def manage_tasks():
    initialize_csv()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Modify Task")
        print("5. Mark Task Done")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            modify_task()
        elif choice == '5':
            mark_task_done()
        elif choice == '6':
            confirmation = input("Are you sure you want to exit? (y/n): ")
            if confirmation.lower() == 'y':
                print("Exiting the Task Manager. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    manage_tasks()