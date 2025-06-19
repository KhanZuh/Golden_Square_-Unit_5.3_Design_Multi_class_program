class Task:

    def __init__(self, description):
        self.description = description
        self.completed = False

    def is_complete(self):
        return self.completed
        
    def mark_complete(self):
        self.completed = True
