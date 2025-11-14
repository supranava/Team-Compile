def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task(s)") # Updated Menu Item
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("------------------------")

def view_tasks(todo_list):
    """Prints the current to-do list."""
    if not todo_list:
        print("\nYour to-do list is empty! Go add some tasks.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(todo_list):
        # 'status' will be '[X]' if complete, or '[ ]' if pending
        status = "[X]" if task.get("completed") else "[ ]"
        print(f"{index + 1}. {status} {task.get('task')}")
    print("--------------------")

def single_add_task(todo_list, new_task):
    """Adds a single new task to the list, defaulting to incomplete."""
    if new_task:
        task_item = {"task": new_task, "completed": False}
        todo_list.append(task_item)
        print(f"Task '{new_task}' added.")
        return True
    else:
        print("Task description cannot be empty. Skipping.")
        return False

def main():
    """Main function to run the To-Do List application."""
    # The list will store dictionaries, e.g., [{'task': 'Buy groceries', 'completed': False}]
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(todo_list)
        
        elif choice == '2':
            print("\n--- Adding Multiple Tasks ---")
            print("Enter tasks one by one. Type 'done' or hit Enter to stop.")
            
            while True:
                task = input("Enter new task: ").strip()
                
                # Check for the exit condition
                if task.lower() in ('done', ''):
                    print("Finished adding tasks.")
                    break
                
                # Add the task
                single_add_task(todo_list, task)

        elif choice == '3':
            view_tasks(todo_list)
            if todo_list:
                task_num = input("Enter the number of the task to mark as complete: ")
                # ... (rest of mark_complete logic)

        elif choice == '4':
            view_tasks(todo_list)
            if todo_list:
                task_num = input("Enter the number of the task to delete: ")
                # ... (rest of delete_task logic)

        elif choice == '5':
            print("\n👋 Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Note: The `mark_complete` and `delete_task` functions (from the previous answer)
# would need to be included here for the full program to run.

if __name__ == "__main__":
    # For demonstration, I'm only showing the updated main function and menu.
    # The full script would include all helper functions.
    
    # You can now test the updated functionality:
    # main() 
    pass