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

    task_information[task_id] = {"Description":task, "Created at": created_at, "Status":"to-do"}

    with open("tasks.json", 'w') as task_file:
        json.dump(task_information, task_file, indent=4)

    print(f"Task added successfully!, assigned id {task_id}")


def delete_task(task_id):
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", 'r') as file:
        task_information = json.load(file)
        try:
            del task_information[task_id]
            with open("tasks.json", 'w') as file:
                json.dump(task_information, file, indent=4)
            
            print("Task deleted successfully!")
        except KeyError:
            print("Key doesn't exist!")


def update_task(task_id, task_description:str):
    
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
        json.dump(task_information, file, indent=4)

    print("Task updated successfully!")


def mark_task(task_id, status):
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", "r") as file:
        task_information = json.load(file)

    task_information[task_id]["Status"] = status

    with open("tasks.json", "w") as file:
        json.dump(task_information, file, indent=4)

    print(f"Task marked as {status}")


def list_all_tasks():

    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return
    
    with open("tasks.json", "r") as file:
        task_information = json.load(file)

    print("\n------Listing All Tasks------\n")
    for key, value in task_information.items():
        print(f"----Task ID {key}----")
        print(f"'{value["Description"]}'")
        print(f"Task status: {value["Status"]}, Created at: {value["Created at"]}, Updated at: {value.get("Updated at")}")
        print()


def list_completed_tasks():
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", "r") as file:
        task_information = json.load(file)

    print("\n------Listing All Completed Tasks------\n")
    for key, value in task_information.items():
        if value["Status"] == "done":
            print(f"----Task ID {key}----")
            print(f"'{value["Description"]}'")
            print(f"Task status: {value["Status"]}, Created at: {value["Created at"]}, Updated at: {value.get("Updated at")}")
            print()


def list_in_progress_tasks():
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", "r") as file:
            task_information = json.load(file)

    print("\n------Listing All In-process Tasks------\n")
    for key, value in task_information.items():
        if value["Status"] == "in-progress":
            print(f"----Task ID {key}----")
            print(f"'{value["Description"]}'")
            print(f"Task status: {value["Status"]}, Created at: {value["Created at"]}, Updated at: {value.get("Updated at")}")
            print()


def list_remaining_tasks():
    if not os.path.isfile("tasks.json"):
        print("File does not exist, please add tasks first!")
        return

    with open("tasks.json", "r") as file:
            task_information = json.load(file)
            
    print("\n------Listing All Remaining Tasks------\n")
    for key, value in task_information.items():
        if value["Status"] != "done":
            print(f"----Task ID {key}----")
            print(f"'{value["Description"]}'")
            print(f"Task status: {value["Status"]}, Created at: {value["Created at"]}, Updated at: {value.get("Updated at")}")
            print()

            
def take_input():

    while True:
        input_info = list(input().split(' ', 1))

        if input_info[0].lower() == "exit":
            break

        if not input_info[0]:
            print("Please write any command in input bar or exit")
            continue

        if len(input_info) > 1:
            function_to_call, task_description = input_info

            if function_to_call.lower() == "update":
                task_info = task_description.split(" ", 1)
                task_id, task_description = task_info
        
            if function_to_call.lower() == "delete":
                task_id = task_description

            if function_to_call.lower() == "mark-in-progress":
                function_to_call = "mark"
                task_id = task_description
                status = "in-progress"

            if function_to_call.lower() == "mark-done":
                function_to_call = "mark"
                task_id = task_description
                status = "done"

            if function_to_call.lower() == "mark-to-do":
                function_to_call = "mark"
                task_id = task_description
                status = "to-do"
        
            task_description = task_description.strip("\"")
        else:
            function_to_call = "".join(input_info)


        match function_to_call:
            case "add":
                add_task(task_description)

            case "delete":
                delete_task(task_id)

            case "update":
                update_task(task_id, task_description)

            case "mark":
                mark_task(task_id, status)

            case "list":
                list_all_tasks()

            case "list-in-progress":
                list_in_progress_tasks()

            case "list-completed":
                list_completed_tasks()

            case "list-remaining":
                list_remaining_tasks()

            case _:
                "Task not added"

if __name__ == "__main__":
    take_input()