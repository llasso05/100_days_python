import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. then print it
random_number = random.randint(0, 2)
chosen_word = word_list[random_number]
print(chosen_word)

# TODO-2 - Ask user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: \n").lower()


# TODO-3 - Check if the letteer the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")