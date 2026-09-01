import os
import json

if __name__ == "__main__":
    class task_tracker_operation:

        def id_generater():
                current_id = 1
                while current_id < 1000:
                    yield current_id
                    current_id += 1

        def add_task(task:str):

            if not os.path.isfile("tasks.json"):
                with open("tasks.json", 'w'):
                    pass

            task_id = next(task_tracker_operation.id_generater())

            task_information = {task_id:task}

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
        
        

        user_task = input()
        add_task(user_task)
            