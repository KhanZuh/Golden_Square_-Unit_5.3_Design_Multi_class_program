import pytest
from lib.Diary_system import DiarySystem
from lib.Todo_list import TodoList
from lib.Diary_entry import DiaryEntry

def test_diary_system_initializes_with_empty_entries_and_todo_list():
    diary_system = DiarySystem()
    assert diary_system.diary_entries == []
    assert isinstance(diary_system.todo_list, TodoList)

def test_add_diary_entry_stores_entry_in_list():
    diary_system = DiarySystem()
    entry = DiaryEntry("My Day", "Today was great")
    diary_system.add_diary_entry(entry)
    assert diary_system.diary_entries == [entry]

def test_select_entries_by_time_returns_entries_within_time_limit():
    diary_system = DiarySystem()
    short_entry = DiaryEntry("Quick note", "Just a short note")  # ~4 words
    long_entry = DiaryEntry("Long story", "This is a very long story with many words and details about my day and experiences")  # ~17 words
    diary_system.add_diary_entry(short_entry)
    diary_system.add_diary_entry(long_entry)

    # When we search for entries we can read in 1 minute at 10 wpm
    suitable_entries = diary_system.select_entries_by_time(1, 10)
    
    # Then we get back only entries that fit within that time limit
    assert suitable_entries == [short_entry]

def test_get_all_phone_numbers_returns_numbers_from_all_entries():

    diary_system = DiarySystem()
    entry1 = DiaryEntry("Meeting", "Called John on 07123456789 about the project")
    entry2 = DiaryEntry("Emergency", "Emergency contact: 07987654321")
    diary_system.add_diary_entry(entry1)
    diary_system.add_diary_entry(entry2)
    
    phone_numbers = diary_system.get_all_phone_numbers()
    
    assert phone_numbers == ["07123456789", "07987654321"]

def test_diary_system_integrates_with_todo_list():

    diary_system = DiarySystem()
    entry = DiaryEntry("Today", "Had a productive day")
    task = Task("Buy groceries")
    
    diary_system.add_diary_entry(entry)
    diary_system.todo_list.add_task(task)
    
    assert diary_system.diary_entries == [entry]
    assert diary_system.todo_list.get_all_tasks() == [task]


def test_complex_scenario_diary_and_todo_management():

    diary_system = DiarySystem()


    quick_entry = DiaryEntry("Morning coffee", "Had great coffee today")  # ~4 words
    medium_entry = DiaryEntry("Lunch meeting", "Met with Sarah about the new project proposal and discussed timelines")  # ~12 words
    long_entry = DiaryEntry("Evening reflection", "Today was incredibly busy with multiple meetings, phone calls, emails, and I managed to complete several important tasks while also finding time to connect with family and friends")  # ~30+ words

    diary_system.add_diary_entry(quick_entry)
    diary_system.add_diary_entry(medium_entry) 
    diary_system.add_diary_entry(long_entry)


    task1 = Task("Call mom")
    task2 = Task("Finish report")
    task3 = Task("Buy milk")
    diary_system.todo_list.add_task(task1)
    diary_system.todo_list.add_task(task2)
    diary_system.todo_list.add_task(task3)

    # Mark one task complete
    task1.mark_complete()

    # When user has 2 minutes, reads 10 words per minute
    readable_entries = diary_system.select_entries_by_time(2, 10)  # Can read ~20 words
    
    # Then we get entries that fit in time limit
    assert readable_entries == [quick_entry, medium_entry]  # Both fit in time limit

    # And we can check remaining tasks
    incomplete_tasks = diary_system.todo_list.get_incomplete_tasks()
    assert incomplete_tasks == [task2, task3]  # task1 was completed
