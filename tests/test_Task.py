from lib.Task import *

def test_task_stores_description():
    description = "Buy groceries" # Arrange
    task = Task(description) # Act
    assert task.description == description # Assert
    