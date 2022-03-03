class Tasks:
    def __init__(self, description, duration):
        self.description = description
        self.duration = duration



    def task_decider(current_task, compared_to_task):
        if current_task.description == "wash dishes":
            if compared_to_task.description == "cook dinner":
                return True
            else: 
                return False
        
        if current_task.description == "cook dinner":
            if compared_to_task.description == "wash dishes":
                return False
            else:
                return True


