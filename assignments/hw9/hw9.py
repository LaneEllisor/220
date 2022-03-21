"""
Name: Lane Ellisor
hw9.py

Problem: Hangman

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def get_words(file_name):
    with open(file_name) as f:
        contents = f.read()
        return contents
print(get_words('words.txt'))

def get_random_word(words):
    return words


