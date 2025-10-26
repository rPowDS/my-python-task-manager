import json
import random

# ------- Configuration -----
# Define the task file name.
TASK_FILE = "tasks.json"

'''To-Do List Application'''

# Build a to do list project that works with CLI


# 1. 
# This list will hold all our to-do tasks.
todo_list = []

# ------- Core Function (Data Management)---------
# 2. Load the tasks from the JSON file.
def load_tasks():
    """Load the tasks from the JSON file."""
    try:
        # 'r' stands for read mode. 'with open' automatically closes the file after the block is executed.
        with open(TASK_FILE, "r") as file:
            # 'json.load' reads the file and converts the JSON data into a Python list.
            return json.load(file)
            # return the list of tasks
    except FileNotFoundError:
        # If the file is not found, return an empty list.
        return []

# 3. Save the tasks to the JSON file.
def save_tasks():
    """Save the tasks to the JSON file. (TASK_FILE is the name of the file.)"""
    # 'w' stands for write mode. (Overwrites the file.)
    print(f"Saving tasks to {TASK_FILE}...")
    with open(TASK_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)




# --------- Task Management Functions ---------
# 4. Add a new task to the list.
def add_task():   # Core Function
    """
    Adds a new task dictionary to the global todo_list.
    """
    # The .append() method adds the item to the very end of the list.
    # Using a dictionary to store the task details.
    # 'task' is the task description.
    # 'completed' is a boolean value that indicates if the task is completed.
    task_description = input("What task would you like to add? ")
    if task_description:
        task = {"task":task_description, "completed":False}
        todo_list.append(task)
        print(f"\n✅ Added task: '{task_description}'")
        
    else:
        print("No task added. Please try again.")

def view_tasks():
    ''' Display all tasks in the todo_list.'''
    print("--- 📋 Your Current Tasks ---")
    if not todo_list:
        print("\nYour to-do list is empty! Add a task (Option 1).")
        return # Stops the function execution here


    # This loop displays all tasks in the todo_list. Not Duplicates
    for index, task in enumerate(todo_list, start=1):
        status = "✅ Done" if task["completed"] else "⌛️ Pending"
        print(f"{index}. [{status}] {task['task']}")
    print("--- End of Tasks ---")

def mark_task_as_complete():
    """Mark a task as complete.
    Using try/except to handle invalid input."""

    view_tasks() # shows the list of tasks to the user

    task_num_str = input("Enter the number of the task to mark as complete: ").strip().lower()

    try:
        task_index = int(task_num_str)

        if 0 < task_index <= len(todo_list):
            if todo_list[task_index - 1]["completed"]:
                print(f"Task {task_index} was already marked as complete.")

            else:
                todo_list[task_index - 1]["completed"] = True
                print(f"\n✅ Task {task_index} marked as complete.")
                save_tasks()

        else: # If the task number is not valid, print an error message.
            print("\n ❌ Invalid task number. Please try again.")

    except ValueError: # If the input is not a valid integer, print an error message.
        print(f"\n ❌ Invalid input. Please enter a valid task number, not '{task_num_str}'.")
        print("\n" + "=" * 35 + "\n")

## ==============================
## UI & Metrics Functions ==============================
## ======================================================


def get_quote():
    """Placeholder for a quote of the day."""
    quotes = [
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "First, solve the problem. Then, write the code. - John Johnson",
        "I will either find a way or make one. - Hannibal Barca",
        "Everything around you was built by people no smarter than you. - Steve Jobs",
        "The best way to predict the future is to invent it. - Alan Kay",
    ]
    return random.choice(quotes)

def display_welcome_message():

    """Display the welcome message."""

    print("\n" + "=" * 35 + "\n")
    print(".    Welcome to the To-Do List    .")
    print("\n" + "=" * 35 + "\n")
    print(f"\t\tQuote of the Day:\n\n {get_quote()}")
    

    ''' Adding a To-Do List Menu '''

    

# --------- Utility: Quote of the Day ---------

    

def display_metrics():
    """Calculating & Displaying the metrics of the to-do list."""
    print("\n" + "=" * 35 + "\n")
    print("---- 📊 Metrics of the To-Do List: ----")
    # This runs inside the loop to stay updated.

    total_tasks = len(todo_list)

    if total_tasks == 0:
        print(" 📋 Your Current Tasks: 0")
        print("No tasks yet. Add a task (Option 1).")
        print("=" * 35 + "\n")
        return

    completed_tasks = sum(1 for task in todo_list if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100

    # Display the metrics of the to-do list.

    print(f". 📝 Total Tasks: {total_tasks}.")
    print(f". ⌛️ Pending Tasks: {pending_tasks}.")
    print(f". ✅ Completed Tasks: {completed_tasks}.")
    print(f". 📈 Progress Rate: {completion_rate:.1f}%.")
    print("\n" + "=" * 35 + "\n")


    #### Display a Bar Chart of the to-do list.
    MAX_GRAPH_WIDTH = 20 # setting constant for the width of the graph
    completed_blocks = int((completion_rate / 100) * MAX_GRAPH_WIDTH)
    pending_blocks = MAX_GRAPH_WIDTH - completed_blocks

    graph = f"[{f'✅' * completed_blocks}{f'⌛️' * pending_blocks}]"
    print(f"    Progress:  {graph}")

    pending_list = [task for task in todo_list if not task["completed"]]

    if pending_list:
        print("\n==== Pending Tasks ====")
        for task in pending_list:
            # Print the task number and the task description.
            print(f"  - {task['task']}")
    print("\n" + "=" * 35 + "\n")


# --- MAIN PROGRAM LOOP ---

def main_menu():
    """
    Displays the main menu and handles user input using a loop.
    """
    
    # Display the metrics of the to-do list.
    display_welcome_message()

    # The 'while True' loop keeps the program running interactively.
    while True:

        # Display the metrics of the to-do list.
        display_metrics()


        print("--- Command-Line To-Do List ---")
        print("1. Add a new task")
        print("2. View all tasks ")
        print("3. Mark a task as complete ")
        print("4. Quit")
        print("-------------------------------")

        # Get the user's input. The input is always a string.
        choice = input("Enter your choice (1-4): ").strip().lower()

        if choice == '1':
            # Ask the user for the task details.
            # Call the function responsible for adding the task.
            add_task()

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            # Call the function responsible for marking the task as complete.
            mark_task_as_complete()
            print("\n" + "=" * 35 + "\n")
            print("Task marked as complete.")
            print("\n" + "=" * 35 + "\n")

        elif choice == '4':
            # Save the tasks to the JSON file.
            save_tasks()
            print("\n" + "=" * 35 + "\n")
            print("Exiting To-Do List. Goodbye!")
            print("\n" + "=" * 35 + "\n")
            print("A Failure is not always a mistake, it's a lesson learned. - Morihei Ueshiba")
            print("\n" + "=" * 35 + "\n")
            # The 'break' keyword stops the 'while True' loop, ending the program.
            break

        else:
            # Error handling for bad input.
            print("\n❌ Invalid choice. Please enter a number from 1 to 4.")


# This check ensures that 'main_menu()' only runs when the script is executed directly.
if __name__ == "__main__":   # This section starts the program
    # Critical: Load the tasks from the JSON file.
    todo_list = load_tasks()
    main_menu()