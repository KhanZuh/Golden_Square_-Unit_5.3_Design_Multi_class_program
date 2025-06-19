from lib.Task import Task


def test_task_stores_description():
    description = "Buy groceries" # Arrange
    task = Task(description) # Act
    assert task.description == description # Assert

def test_new_task_starts_as_incomplete():
    task = Task("Buy groceries")
    result = task.is_complete()
    assert result == False

def test_task_is_complete_when_marked_complete():
    task = Task("Buy groceries")
    task.mark_complete()
    result = task.is_complete()
    assert result == True


    