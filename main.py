import os
import json

if __name__ == "__main__":
    class task_tracker_operation:

        @staticmethod
        def id_generater():
                current_id = 1
                while current_id < 1000:
                    yield current_id
                    current_id += 1

        global task_id; 
        task_id = next(id_generater())            

        @staticmethod
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
        
        @staticmethod
        def take_input():
            while True:
                input_info = list(input().split('"'))
                input_info.pop()
                input_info[0].strip()
                if input_info[0].lower() == "exit":
                    break
                function_to_call, task_description = input_info

                match function_to_call:
                    case "add":
                        task_tracker_operation.add_task(task_description)
        


        take_input()
        # while True:
        #     user_task = input()
        #     if len(user_task) == 0:
        #         break 
        #     add_task(user_task)
            