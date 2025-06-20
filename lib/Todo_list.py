class TodoList:

    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        if task is None:
            raise Exception("Cannot add None as a task")  # Changed from ValueError to Exception
        self.tasks.append(task)
    
    def get_all_tasks(self):
        return self.tasks

    
    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_complete()]
    
    def get_complete_tasks(self):
        return [task for task in self.tasks if task.is_complete()]
    
    def remove_task(self, task):
        self.tasks.remove(task)

    def get_task_count(self):
        return {"total" : len(self.tasks), "complete" : len(self.get_complete_tasks()), "incomplete" : len(self.get_incomplete_tasks())}
    
    def clear_completed_tasks(self):
        # show only incomplete tasks
        self.tasks = [task for task in self.tasks if not task.is_complete()]



