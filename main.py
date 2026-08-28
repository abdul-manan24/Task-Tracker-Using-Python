if __name__ == "__main__":
    class task_tracker_operation:

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
    class utility_functions:
        @staticmethod
        def id_generater():
            current_id = 1
            while current_id < 1000:
                yield current_id
                current_id += 1

    class main:
        current_id = next(utility_functions.id_generater())
        print(current_id)
            