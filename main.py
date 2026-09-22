import os
import json

def id_generater():
        current_id = 1
        while current_id < 1000:
            yield current_id
            current_id += 1

      

def add_task(task:str):

    if not os.path.isfile("tasks.json"):
        with open("tasks.json", 'w'):
            pass
    
    global task_id
    task_information = {task_id:{"Description":task}}


    with open("tasks.json", 'a') as task_file:
        json.dump(task_information, task_file, indent=2)

def delete_task():
    pass

def update_task():
    pass

def list_all_tasks():
    pass

def list_completed_tasks():
    pass

def list_inprogress_tasks():
    pass

def list_remaining_tasks():
    pass

def take_input():
    global task_id
    while True:
        input_info = list(input().split(' ', 1))
        task_id = next(id_generater())      
        if input_info[0].lower() == "exit":
            break

        if not input_info[0]:
            print("Please write any command in input bar or exit")
            continue

        function_to_call, task_description = input_info
        # print(function_to_call, task_description)

        match function_to_call:
            case "add":
                add_task(task_description)
            case _:
                "Task not added"



take_input()
# while True:
#     user_task = input()
#     if len(user_task) == 0:
#         break 
#     add_task(user_task)

if __name__ == "__main__":
    pass