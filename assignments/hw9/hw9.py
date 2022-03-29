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
    for line in lines:
        words.append(line)
    file.close
    return words

def get_random_word(words):
    random_index = randint(0, len(words)-1)
    random_word = words[random_index]
    return random_word


def letter_in_secret_word(letter, secret_word):
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            return True
        else:
            return False


def already_guessed(letter, guesses):
    for letter in guesses:
        if letter in guesses:
            return True
        else:
            return False


def make_hidden_secret(secret_word, guesses):
    pass


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)