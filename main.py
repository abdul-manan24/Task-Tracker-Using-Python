import os
import json
from datetime import datetime
 
def add_task(task:str):
    created_at = datetime.now()
    created_at = created_at.strftime("%d-%m-%Y %I:%M %p")
    if not os.path.isfile("tasks.json"):
        with open("tasks.json", 'w'):
            pass

        task_information = dict()
        task_id = len(task_information) + 1
    else:
        with open('tasks.json', 'r') as file:
            task_information = json.load(file)
        task_id = len(task_information) + 1

    while str(task_id) in task_information.keys():
        task_id += 1

    # print(task_id in task_information.keys())
    # print(type(task_id))

    task_information[task_id] = {"Description":task, "Created at": created_at, "status":"Pending"}

    # print(task_information)
    with open("tasks.json", 'w') as task_file:
        json.dump(task_information, task_file, indent=2)

    print(f"Task added successfully!, assigned id {task_id}")

def delete_task(task_id:int):
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", 'r') as file:
        task_information = json.load(file)
        try:
            del task_information[task_id]
            with open("tasks.json", 'w') as file:
                json.dump(task_information, file, indent=2)
            
            print("Task deleted successfully!")
        except KeyError:
            print("Key doesn't exist!")

def update_task(task_id:int, task_description:str):
    updated_at = datetime.now()
    updated_at = updated_at.strftime("%d-%m-%Y %I:%M %p")

    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", "r+") as file:
    
        task_information = json.load(file)
        try:
            task_information[task_id]["Description"] = task_description
            task_information[task_id]["Updated at"] = updated_at
        except KeyError:
            print("No any with that key exists!")
            
    with open("tasks.json", 'w') as file:
        json.dump(task_information, file, indent=2)

    print("Task updated successfully!")

def list_all_tasks():
    pass

def list_completed_tasks():
    pass

def list_inprogress_tasks():
    pass

def list_remaining_tasks():
    pass

def take_input():

    while True:
        input_info = list(input().split(' ', 1))

        if input_info[0].lower() == "exit":
            break

        if not input_info[0]:
            print("Please write any command in input bar or exit")
            continue

        function_to_call, task_description = input_info

        if function_to_call.lower() == "update":
            task_info = task_description.split(" ", 1)
            task_id, task_description = task_info

        elif function_to_call.lower() == "delete":
            task_id = task_description

        task_description = task_description.strip("\"")

        match function_to_call:
            case "add":
                add_task(task_description)
            case "delete":
                delete_task(task_id)
            case "update":
                update_task(task_id, task_description)
            case _:
                "Task not added"


take_input()

if __name__ == "__main__":
    pass