# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences
> I want to read my past diary entries

> As a user
> So that I can reflect on my experiences in my busy day
> I want to select diary entries to read based on how much time I have and my reading speed

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary entries>


## 2. Design the Class System

```
Identify the nouns (they become classes)
1. diary
2. diary entries
3. experiences
4. tasks
5. todo list, 
6. mobile phone numbers
7. contacts

Identify the verbs (they become methods)
1. record
2. read 
3. select based on time/reading speed
4. keep track
5. see a list


Identify responsibilities
- A diary system owns multiple diary entries
- A todo list owns multiple tasks
- The overall system needs to coordinate both

Implementation
- DiarySystem as the main coordinator (because user stories suggest one integrated system)
- Separate TodoList (because it has its own distinct behavior)
- DiaryEntry knows how to extract phone numbers (because the data lives there)



```

```
┌─────────────────────────────────┐
│ DiarySystem                     │
│                                 │
│ - diary_entries: []             │
│ - todo_list: TodoList           │
│                                 │
│ - add_diary_entry(entry)        │
│ - get_all_entries()             │
│ - select_entries_by_time(mins,  │
│   reading_speed)                │
│ - get_all_phone_numbers()       │
└─────────────┬───────────────────┘
              │
              │ owns/manages
              ▼
┌─────────────────────────────────┐
│ DiaryEntry                      │
│                                 │
│ - title: string                 │
│ - contents: string              │
│ - date: date                    │
│                                 │
│ - count_words()                 │
│ - reading_time(reading_speed)   │
│ - extract_phone_numbers()       │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ TodoList                        │
│                                 │
│ - tasks: []                     │
│                                 │
│ - add_task(task)                │
│ - mark_complete(task)           │
│ - get_incomplete_tasks()        │
└─────────────┬───────────────────┘
              │
              │ owns/manages
              ▼
┌─────────────────────────────────┐
│ Task                            │
│                                 │
│ - description: string           │
│ - completed: boolean            │
│                                 │
│ - mark_complete()               │
│ - is_complete()                 │
└─────────────────────────────────┘

```

_Also design the interface of each class in more detail._

```python
class DiarySystem:
    # User-facing properties:
    #   diary_entries: list of DiaryEntry instances
    #   todo_list: TodoList instance

    def __init__(self):
        # Side-effects:
        #   Sets up empty diary_entries list and creates TodoList
        pass # No code here yet

    def add_diary_entry(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the diary_entries list
        pass # No code here yet

    def get_all_entries(self):
        # Returns:
        #   A list of all DiaryEntry instances
        pass

    def select_entries_by_time(self, minutes, reading_speed):
        # Returns:
        #   A list of DiaryEntry instances that can be read in the given time
        pass

    def get_all_phone_numbers(self):
        # Returns:
        #   A list of all phone numbers found in all diary entries
        pass


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string
    #   date: ??? (date object or string?)

    def __init__(self, title, contents):
        # Side-effects:
        #   Sets the title and contents properties
        #   Sets the date property to current date
        pass

    def count_words(self):
        # Returns:
        #   An integer count of words in the contents
        pass

    def reading_time(self, reading_speed):
        # Returns:
        #   An integer representing minutes needed to read this entry
        pass

    def extract_phone_numbers(self):
        # Returns:
        #   A list of phone number strings found in the contents
        pass


class TodoList:
    # User-facing properties:
    #   tasks: list of Task instances

    def __init__(self):
        # Side-effects:
        #   Sets up empty tasks list
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Adds the task to the tasks list
        pass # No code here yet

    def mark_complete(self, task):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Marks the given task as complete
        pass # No code here yet

    def get_incomplete_tasks(self):
        # Returns:
        #   A list of Task instances that are not completed
        pass # No code here yet

    def get_all_tasks(self):
        # Returns:
        #   A list of all Task instances
        pass # No code here yet


class Task:
    # User-facing properties:
    #   description: string
    #   completed: boolean

    def __init__(self, description):
        # Parameters:
        #   description: string
        # Side-effects:
        #   Sets the description property
        #   Sets completed to False
        pass # No code here yet

    def mark_complete(self):
        # Side-effects:
        #   Sets completed to True
        pass # No code here yet

    def is_complete(self):
        # Returns:
        #   Boolean indicating if task is completed
        pass # No code here yet

```

## How to think out your test cases (Integration and Unit)

# For Integration Tests:

- Look at your user stories - what combinations haven't you tested?
- Think like a real user - what would they actually do?
- Create realistic scenarios with specific, verifiable data


# For Unit Tests:

- Go method by method through each class
- Test the happy path (normal usage)
- Test edge cases (empty, zero, etc.)
- Use simple, verifiable examples (like 5 words you can count)

## 3. Create Examples as Integration Tests

### 🧠 Thought process 
Look at user stories and look at whats not being tested:
- ✅ Adding diary entries
- ✅ Reading entries by time
- ✅ Getting phone numbers
- ❌ Todo list + diary working together ← This is missing!

What would a real user do?
- A real person would have BOTH diary entries AND tasks
- They'd want to manage their time (reading + tasks)
- They'd mark tasks complete throughout the day

Realistic scenarios for testing
- Different entry lengths (quick, medium, long)
- Realistic scenarios ("busy day", "2 minutes available")
- Mixed completed/incomplete tasks

```python
"""
Given a diary system
When we add a diary entry
We see that entry reflected in the diary entries list
"""
diary_system = DiarySystem()
entry = DiaryEntry("My first day", "Today was amazing! I learned Python.")
diary_system.add_diary_entry(entry)
diary_system.diary_entries # => [entry]


"""
Given a diary system with multiple entries
When we search for entries we can read in a given time
We get back entries that fit within that time limit
"""
diary_system = DiarySystem()
short_entry = DiaryEntry("Quick note", "Just a short note")  # ~4 words
long_entry = DiaryEntry("Long story", "This is a very long story with many words and details about my day and experiences")  # ~17 words
diary_system.add_diary_entry(short_entry)
diary_system.add_diary_entry(long_entry)
# If reading speed is 10 words per minute and we have 1 minute
suitable_entries = diary_system.select_entries_by_time(1, 10)
suitable_entries # => [short_entry]  # Only the short one fits


"""
Given a diary system with entries containing phone numbers
When we get all phone numbers
We see all phone numbers from all entries
"""
diary_system = DiarySystem()
entry1 = DiaryEntry("Meeting", "Called John on 07123456789 about the project")
entry2 = DiaryEntry("Emergency", "Emergency contact: 07987654321")
diary_system.add_diary_entry(entry1)
diary_system.add_diary_entry(entry2)
diary_system.get_all_phone_numbers() # => ["07123456789", "07987654321"]


"""
Given a diary system with todo list
When we add tasks and diary entries
We can access both independently
"""
diary_system = DiarySystem()
entry = DiaryEntry("Today", "Had a productive day")
task = Task("Buy groceries")
diary_system.add_diary_entry(entry)
diary_system.todo_list.add_task(task)
diary_system.diary_entries # => [entry]
diary_system.todo_list.get_all_tasks() # => [task]


"""
Given a diary system with multiple diary entries and a todo list with tasks
When we have a busy day and want to read entries that fit our available time
And we also want to check our incomplete tasks
We can manage both diary reading and task management together
"""
diary_system = DiarySystem()

# Add some diary entries
quick_entry = DiaryEntry("Morning coffee", "Had great coffee today")  # ~4 words
medium_entry = DiaryEntry("Lunch meeting", "Met with Sarah about the new project proposal and discussed timelines")  # ~12 words
long_entry = DiaryEntry("Evening reflection", "Today was incredibly busy with multiple meetings, phone calls, emails, and I managed to complete several important tasks while also finding time to connect with family and friends")  # ~30+ words

diary_system.add_diary_entry(quick_entry)
diary_system.add_diary_entry(medium_entry) 
diary_system.add_diary_entry(long_entry)

# Add some tasks
task1 = Task("Call mom")
task2 = Task("Finish report")
task3 = Task("Buy milk")
diary_system.todo_list.add_task(task1)
diary_system.todo_list.add_task(task2)
diary_system.todo_list.add_task(task3)

# Mark one task complete
task1.mark_complete()

# User has 2 minutes, reads 10 words per minute
readable_entries = diary_system.select_entries_by_time(2, 10)  # Can read ~20 words
readable_entries # => [quick_entry, medium_entry]  # Both fit in time limit

# Check remaining tasks
incomplete_tasks = diary_system.todo_list.get_incomplete_tasks()
incomplete_tasks # => [task2, task3]  # task1 was completed


```

## 4. Create Examples as Unit Tests

### 🧠 Thought process 

Go through EACH class and asked "What does this class need to do"?

For ```DiaryEntry```:
- ✅ Store title → test the property
- ✅ Store contents → test the property
- ✅ Count words → test with known word count
- ✅ Calculate reading time → test with simple math I can verify
- ✅ Find phone numbers → test with known phone numbers
- ✅ Handle no phone numbers → test edge case (empty list)



```python
# UNIT TEST EXAMPLES

# ===== DiaryEntry Unit Tests =====

"""
Given a diary entry with title and contents
We see the title reflected in the title property
"""
entry = DiaryEntry("My Day", "Today was great")
entry.title # => "My Day"


"""
Given a diary entry with title and contents
We see the contents reflected in the contents property
"""
entry = DiaryEntry("My Day", "Today was great")
entry.contents # => "Today was great"


"""
Given a diary entry with contents
When we count words
We get the correct word count
"""
entry = DiaryEntry("Test", "This is a test entry")
entry.count_words() # => 5


"""
Given a diary entry and a reading speed
When we calculate reading time
We get the time in minutes needed to read the entry
"""
entry = DiaryEntry("Test", "This is a test entry with ten words total")  # 10 words
entry.reading_time(5) # => 2 (minutes, since 10 words ÷ 5 words/min = 2 min)


"""
Given a diary entry with phone numbers in the contents
When we extract phone numbers
We get a list of all phone numbers found
"""
entry = DiaryEntry("Contacts", "Called 07123456789 and also 07987654321 today")
entry.extract_phone_numbers() # => ["07123456789", "07987654321"]


"""
Given a diary entry with no phone numbers
When we extract phone numbers
We get an empty list
"""
entry = DiaryEntry("No phones", "Just a regular diary entry")
entry.extract_phone_numbers() # => []

# ===== Task Unit Tests =====

"""
Given a task with a description
We see the description reflected in the description property
"""
task = Task("Buy groceries")
task.description # => "Buy groceries"


"""
Given a new task
It starts as not completed
"""
task = Task("Buy groceries")
task.is_complete() # => False


"""
Given a task
When we mark it complete
It becomes completed
"""
task = Task("Buy groceries")
task.mark_complete()
task.is_complete() # => True

# ===== TodoList Unit Tests =====

"""
Given an empty todo list
When we add a task
We see that task in the tasks list
"""
todo_list = TodoList()
task = Task("Buy milk")
todo_list.add_task(task)
todo_list.tasks # => [task]


"""
Given a todo list with completed and incomplete tasks
When we get incomplete tasks
We only see the incomplete ones
"""
todo_list = TodoList()
task1 = Task("Buy milk")
task2 = Task("Walk dog")
task1.mark_complete()
todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.get_incomplete_tasks() # => [task2]


"""
Given a todo list with multiple tasks
When we get all tasks
We see all tasks regardless of completion status
"""
todo_list = TodoList()
task1 = Task("Buy milk")
task2 = Task("Walk dog")
task1.mark_complete()
todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.get_all_tasks() # => [task1, task2]
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
