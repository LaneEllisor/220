"""
Name: Lane Ellisor
hw9.py

Problem: Hangman

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def get_words(file_name):
    file = open(file_name, "r")
    words = []
    for line in file:
        words.append(line.strip())
    return words

def get_random_word(words):
    random_word = words[randint(1, len(words))]
    return random_word


def letter_in_secret_word(letter)


