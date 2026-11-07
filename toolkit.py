# ==========================================
# Personal Mini-Toolkit Project
# Author: Yunan Natalla Lamina
# Repository: plp-python-week8
# ==========================================

def todo_list_tool():
    """Manages a dynamic to-do list where users can view, add, and remove tasks."""
    tasks = ["Review Python notes", "Commit project to GitHub"]
    print("\n--- Dynamic To-Do List ---")
    
    while True:
        print(f"\nCurrent Tasks: {tasks}")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            print(f"\nYou currently have {len(tasks)} tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == '2':
            new_task = input("Enter the task to add: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success: '{new_task}' has been added to your list.")
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            task_to_remove = input("Enter the exact task name to remove: ").strip()
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"Success: '{task_to_remove}' has been removed.")
            else:
                print(f"Error: '{task_to_remove}' was not found in your list.")
        elif choice == '4':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please select a valid option between 1 and 4.")


def even_number_counter_tool():
    """Loops through a range of numbers up to a user-defined limit and counts the even numbers."""
    print("\n--- Even Number Counter ---")
    try:
        limit = int(input("Enter a positive whole number as your upper limit: "))
        if limit < 1:
            print("Please enter a number greater than or equal to 1.")
            return
        
        even_count = 0
        even_numbers = []
        
        for num in range(1, limit + 1):
            if num % 2 == 0:
                even_count += 1
                even_numbers.append(num)
                
        print(f"Between 1 and {limit}, there are {even_count} even numbers.")
        print(f"The even numbers are: {even_numbers}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


def simple_calculator_tool():
    """Performs basic arithmetic operations using user-provided numbers and an operator."""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is undefined.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print(f"Error: '{operator}' is not a valid operator.")
    except ValueError:
        print("Invalid input! Please enter numeric values for the numbers.")


def main():
    print("=========================================")
    print("   WELCOME TO YOUR PERSONAL MINI-TOOLKIT ")
    print("=========================================")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Dynamic To-Do List")
        print("2. Even Number Counter")
        print("3. Simple Calculator")
        print("4. Quit")
        
        choice = input("Please select an option (1-4): ").strip()
        
        if choice == '1':
            todo_list_tool()
        elif choice == '2':
            even_number_counter_tool()
        elif choice == '3':
            simple_calculator_tool()
        elif choice == '4':
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("\nOops! That is not a valid menu choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()