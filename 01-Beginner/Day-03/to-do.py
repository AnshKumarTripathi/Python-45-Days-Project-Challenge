# Day 3: To-Do List CLI Application

"""
Theory:
A command-line interface (CLI) to-do list application allows users to manage their tasks from the terminal.
This project will help you understand the following concepts:

1. Input Handling:
   - Reading user inputs from the terminal.

2. Data Storage:
   - Storing tasks in a list or dictionary.

3. Control Flow:
   - Using loops and conditionals to manage the application flow.

4. Basic Functions:
   - Creating functions for adding and removing tasks.
   - Displaying the list of tasks.
"""

"""
Hints:
1. Input Handling:
   - Use input() to read user commands.
   - Parse commands to determine the action (e.g., add or remove a task).

2. Data Storage:
   - Store tasks in a list or dictionary.
   - Consider using a dictionary with task IDs as keys for easier removal.

3. Control Flow:
   - Use a while loop to keep the application running.
   - Use if statements to handle different commands.

4. Basic Functions:
   - Write a function to add a task to the list.
   - Write a function to remove a task by its ID or name.
   - Write a function to display the current list of tasks.
"""

toDoList = []

def addTask():
    task = input("Enter your To-DO task: ")
    toDoList.append(task)

def removeTask():
    print("\n Here is the total Task of the TO-DO list: \n", toDoList,"\n")
    removeTaskName = input("Enter the task you want to remove: ")
    if removeTaskName in toDoList:
        toDoList.remove(removeTaskName)
        print("After removal, the list looks like this: \n", toDoList)
    else:
        print(f"Task '{removeTaskName}' not found in the to-do list.")

def viewTask():
    print("\n Here is the total Task of the TO-DO list: \n", toDoList, "\n")

while True:
    userChoice = input("Do you want to add a task? If yes, then write 'y': ")
    
    if userChoice.lower() == 'y':
        addTask()
        intInput = int(input("How many more tasks do you want to add? "))
        for _ in range(intInput):
            addTask()

        while True:
            inputInt = int(input("\n Press 1 to view the to-do list \nPress 2 to remove a task \nPress 3 to add more tasks \nPress any other key to exit the application: "))
            
            match inputInt:
                case 1:
                    viewTask()
                case 2:
                    removeTask()
                case 3:
                    addTask()
                case _:
                    # Exit the application
                    break
    else:
        break

print("Thanks for using the application")
