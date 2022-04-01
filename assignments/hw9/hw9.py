"""
Name: Lane Ellisor
hw9.py

Problem: Hangman

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
def get_words(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    words = []
    for words in lines:
        words.append(words)
    return words

def get_random_word(words):
    random_index = randint(0, len(words)-1)
    random_word = words[random_index]
    return random_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    hidden_word = ""
    for letter in range(len(secret_word)):
        if letter not in guesses:
            secret_word = secret_word.replace(letter, "_")
        else:
            return None
    for letter in range(len(secret_word)):
        hidden_word = " ".join(hidden_word)
    return hidden_word


def won(guessed):
    if "_" not in guessed:
        return True
    else:
        return False





def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)