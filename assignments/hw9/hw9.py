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
    words = []
    for word in file:
        words.append(word)
    return words

def get_random_word(words):
    random_index = randint(0, len(words)-1)
    random_word = words[random_index]
    return random_word[:-1]


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
    for letter in secret_word:
        if letter in guesses:
            pass
        else:
            secret_word = str(secret_word.replace(letter, "_ "))
    for letter in secret_word:
        hidden_word += letter + " "
    return hidden_word


def won(guessed):
    if "_" not in guessed:
        return True
    else:
        return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    attempts = 6
    guess_list = []

    hidden_word = make_hidden_secret(secret_word, guesses)

    while not won(hidden_word) and attempts > 0:
        guessed_letter = input("Guess a letter:   ")

        if not already_guessed(letter, guesses) and letter in secret_word:
            guess_list.append(letter)
            hidden_word = make_hidden_secret(secret_word, guesses)
            return hidden_word
        if not already_guessed(letter, guesses) and letter not in secret_word:
            guessed_list.append(letter)
            attempts -= 1
            hidden_word = make_hidden_secret(secret_word, guesses)

            return hidden_word

        else:
            return "Error"

    if won(hidden_word):
        return "You won!"
    if attempts == 0:
        return "You lost. The word was" + str(secret_word)
    else:
        pass



if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)