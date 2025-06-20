import pytest
from datetime import date 
from lib.Diary_entry import DiaryEntry

def test_stores_title_correctly():
    entry = DiaryEntry("My day", "Today was great")
    assert entry.title == "My day"

def test_contents_stores_correctly():
    entry = DiaryEntry("My day", "Today was great")
    assert entry.contents == "Today was great"

def test_sets_date_to_today():
    entry = DiaryEntry("My day", "Today was great")
    assert entry.date ==  date.today()


def test_count_words_gives_correct_word_count():
    entry = DiaryEntry("My day", "Today was great")
    assert entry.count_words() == 5

def test_reading_time_calculates_minutes_based_on_entry_and_reading_speed():
    entry = DiaryEntry("My day", "Today was great")
    assert entry.reading_time(5) == 1

def test_extract_phone_numbers_returns_all_numbers():
    entry = DiaryEntry("Meeting Notes", "Contact Dave on 07700 900123 about the project. Also need to call the office on 020 7946 0958 tomorrow.")
    result = entry.extract_phone_numbers()
    assert result == ["07700900123", "02079460958"]

def test_extract_phone_numbers_ignores_invalid_numbers():

    # Arrange
    entry = DiaryEntry("Mixed", "My number is 07123456789 but not 0123456789 or 447123456789")
    
    # Act
    phone_numbers = entry.extract_phone_numbers()
    
    # Assert
    # Only the valid UK mobile format should be extracted
    assert phone_numbers == ["07123456789"]