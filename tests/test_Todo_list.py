from lib.Todo_list import TodoList
from lib.Task import Task
import pytest

def test_list_is_empty_at_initilization():
    todo_list = TodoList()
    assert todo_list.tasks == []

def test_adding_none_task_raises_error():
    todo_list = TodoList()
    with pytest.raises(Exception, match="Cannot add None as a task"):
        todo_list.add_task(None)

def test_adding_task_shows_up_in_todo_list():
    todo_list = TodoList()
    task = Task("Buy milk")
    todo_list.add_task(task)
    assert task in todo_list.tasks

def test_getting_incomplete_tasks_returns_incomplete_tasks():
    todo_list = TodoList()
    incomplete_task = Task("Buy milk")
    complete_task = Task("Do laundry")
    complete_task.mark_complete()  
    todo_list.add_task(incomplete_task)
    todo_list.add_task(complete_task)
    result = todo_list.get_incomplete_tasks()
    assert result == [incomplete_task]

def test_get_complete_tasks_returns_only_completed():
    todo_list = TodoList()
    incomplete_task = Task("Buy milk")
    complete_task = Task("Do laundry")
    complete_task.mark_complete()
    todo_list.add_task(incomplete_task)
    todo_list.add_task(complete_task)
    
    result = todo_list.get_complete_tasks()
    assert result == [complete_task]
    assert incomplete_task not in result

def test_remove_task_removes_existing_task():
    todolist = TodoList()
    task = Task("Buy milk")
    todolist.add_task(task)

    todolist.remove_task(task)
    assert task not in todolist.tasks

def test_get_task_count_returns_correct_counts():
    todo_list = TodoList()
    incomplete_task1 = Task("Buy milk")
    incomplete_task2 = Task("Walk dog")
    complete_task = Task("Do laundry")
    todo_list.add_task(incomplete_task1)
    todo_list.add_task(incomplete_task2)
    todo_list.add_task(complete_task)
    complete_task.mark_complete()

    counts = todo_list.get_task_count()
    assert counts['total'] == 3
    assert counts['complete'] == 1
    assert counts['incomplete'] == 2

def test_clear_completed_tasks_removes_only_completed():
    todo_list = TodoList()
    incomplete_task = Task("Buy milk")
    complete_task1 = Task("Do laundry")
    complete_task2 = Task("Take out trash")

    todo_list.add_task(incomplete_task)
    todo_list.add_task(complete_task1)
    todo_list.add_task(complete_task2)
    
    complete_task1.mark_complete()
    complete_task2.mark_complete()
    
    todo_list.clear_completed_tasks()
    
    assert incomplete_task in todo_list.tasks
    assert complete_task1 not in todo_list.tasks
    assert complete_task2 not in todo_list.tasks
