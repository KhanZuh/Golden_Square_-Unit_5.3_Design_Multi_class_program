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
        pattern = r'\d+(?:\s+\d+)+'
        matches = re.findall(pattern, self.contents)
        print(f"Regex found: {matches}") 
        cleaned_matches = []
        for match in matches:
            print(f"Processing: '{match}'")
            cleaned_string = match.replace(" ", "")
            print(f"Cleaned to: '{cleaned_string}'")
            cleaned_matches.append(cleaned_string)
            print(f"List now contains: {cleaned_matches}")

        print(f"Final result: {cleaned_matches}")
        return cleaned_matches
    