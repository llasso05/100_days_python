# Select difficulty function
import random


def select_difficulty():
    """Returns attempts based of difficulty selected by user"""
    difficulty = ""
    while difficulty != "easy" or difficulty != "hard":
        difficulty = input("Welcome to guess the number \n Select Difficulty (Easy/Hard): ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Please type 'Easy' or 'Hard'")


def number_guess():
    number = random.randint(1, 100)
    return number



