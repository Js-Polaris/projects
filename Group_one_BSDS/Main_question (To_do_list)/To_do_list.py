##KABUNGA AKRAM JOSHUA M25B38/004
## OBAR DANIEL M25B38/014
##ABI MIREMBE JOY KIGOZI M25B38/022
##KIBIRIGE SAMUEL M25B38/034
##NAMAYA BRENDA HANNAH M25B38/043

import json
from colorama import Fore, init
from datetime import datetime ## 
import os ##This is used to check whether the file is present in the set lab

init(autoreset =True) ##initializing colorama enables use to use the colors on text properly and autorests color to black once doen applying to text. Without the modeule cannot work on windows

TaskFile ="tasks.json"

def load_tasks():
    if os.path.exists(TaskFile):
        with open(TaskFile, "r") as f:
            return json.load(f)
    return []

def save_task():
    with open(TaskFile, "w" ) as f: ## overwites the list if it is not there. The file, that is.
        json.dump(tasks, f, indent =3) ##add the tasks into our TaskFile and give it a spicing of 3 btn items

tasks =load_tasks()

def main():
    while True:
        print("\n=== To Do List Menu ===")
        print("1. Add a task")
        print("2. View added Tasks")
        print("3. Delete a Task")
        print("4. Mark Task as done")
        print("5. Exit")

        try:
            choice = int(input("Please make your choice here: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            delete()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def add():
    while True:
        print("\n=== Add Task ===")
        task = input("Enter desired task: ")
        category = input("Enter category of the task (school, Home, Personal, Ambiguous):").lower().strip()
        
        due_input = input("When do you wish to accomplish the task added? (YYYY-MM-DD HH:MM): ")
                
        due =None ##sets our duetime to nothing so that it can be populated or entered by user hence stored with the task
        try:
            if due_input:
                due = datetime.strptime(due_input, "%Y-%m-%d %H:%M").strftime("%Y %m %d %H:%M") ## changes the time into the datetime format for the programme and then converts it to the format readable to us
        except ValueError:
            print("Invalid date and time format.")
        
        ##mini tasks
        subtasks =[]
        while True:
            sub_task= input("Please enter a smaller task here. Skip by pressing enter: ")
            if sub_task:
                subtasks.append(sub_task) ##adds the subtask to the section "sub_task"
            else:
                break
        
        tasks.append({
            "task": task, 
            "done": False, 
            "category": category, 
            "due": due, 
            "subtasks": subtasks
            }) ## adds the tasks in form of a dictionary with their respective variables 
        save_task()
        print(Fore.GREEN + f"Task ' {task}' was added successfully!")## this will print the successfully addede task in the color green

        continuation = input("Would you like to add another task? (yes/no): ").lower() ##will make the input into lowercase letters and won't cause a crash when entered in another case
        if continuation.lower() != "yes":
            break

def view():
    print("\n=== Your Tasks ===")
    if not tasks:
        print("No tasks added yet.")
    else:
        for idx, task in enumerate(tasks, 1):
            status_color = Fore.GREEN if task["done"] else Fore.RED
            status = "✅ Done" if task["done"] else "❌ Not done"
            category =f"[{task['category']}]" if task["category"] else "" ##calls the category added for the respective task and if it is empty it prints an empty string
            due = f"(Due: {task['due']})" if  task["due"] else ""
            print(status_color + f"{idx}.{task['task']} {category} {due}- {status}")##prints the task in green since it the status_color we chose. Prinst the task, due date, status and index
            
            if task.get("subtasks"):
                for sub_idx, sub in enumerate(task["subtasks"]):
                    print(Fore.YELLOW + f" ~Subtask {sub_idx +1}: {sub}")

def delete():
    view()
    try:
        index = int(input("Enter the number of the task to delete: "))
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(Fore.LIGHTMAGENTA_EX + f"Deleted task: '{removed_task['task']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    view()
    try:
        index = int(input("Enter the number of the task to mark as done: "))
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(Fore.CYAN + f"Marked task '{tasks[index]['task']}' as done.")
            save_task()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
main()
