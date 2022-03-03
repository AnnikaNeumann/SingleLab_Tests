class Tasks:
    def __init__(self, description, duration):
        self.description = description
        self.duration = duration



    def task_decider(current_task, compared_to_task):

        compared_task = compared_to_task.description
        if current_task.description == "wash dishes":
            if compared_task == "cook dinner" or compared_task == "wash clothes":
                return True
            else: 
                return False
        
        if current_task.description == "cook dinner":
            if compared_task == "wash dishes" or compared_task == "wash clothes":
                return False
            else:
                return True

        if current_task.description == "clean windows":
            if compared_task == "wash dishes" or compared_task == "do ironing":
                return True
            else:
                return False

        if current_task.description == "wash clothes":
            if compared_task == 'wash dishes' or compared_task == "do ironing":
                return False
            else:
                return True

        if current_task.description == "do ironing":
            if compared_task == "wash clothes" or compared_task == "wash dishes":
                return True
            else:
                return False

        

