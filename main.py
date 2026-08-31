if __name__ == "__main__":
    class task_tracker_operation:

        def id_generater():
                current_id = 1
                while current_id < 1000:
                    yield current_id
                    current_id += 1

        def add_task(task:str):
            task_information = {}
            with open("tasks.json", 'w') as task_file:
                pass

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
        
        current_id = next(id_generater())
        print(current_id)
            