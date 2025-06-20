from datetime import datetime
import math
import re

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.date = datetime.now().date() # Automatically set the date to today when entry is created 

    def count_words(self):
        words = self.title + " " + self.contents
        return len(words.split())
    
    def reading_time(self, wpm):  
        words = self.count_words()  
        time_in_minutes = math.ceil(words/wpm)
        return time_in_minutes
    
    def extract_phone_numbers(self):
        pattern = r'\b\d+(?:\s+\d+)*\b'
        matches = re.findall(pattern, self.contents)
        print(f"Regex found: {matches}") 
        valid_numbers = []
        for match in matches:
            print(f"Processing: '{match}'")
            cleaned_match = match.replace(" ", "")
            print(f"Cleaned to: '{cleaned_match}'")
            if len(cleaned_match) == 11:
                valid_numbers.append(cleaned_match)
            print(f"List now contains: {valid_numbers}")

        print(f"Final result: {valid_numbers}")
        return valid_numbers

