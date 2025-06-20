from lib.Todo_list import TodoList

class DiarySystem:

    def __init__(self):
        self.diary_entries = []
        self.todo_list = TodoList()

    def add_diary_entry(self, entry):
        self.diary_entries.append(entry)

