from Day12.art import win, lose, intro
from Day12.src import select_difficulty, number_guess

print(intro)

attempts = select_difficulty()
secret_number = number_guess()

while attempts > 0:
    # print(secret_number)
    user_guess = int(input("Select a number from 1 to 100: "))
    if user_guess == secret_number:
        print(win)
        break
    elif user_guess > secret_number:
        print("To High")
        attempts -= 1
    elif user_guess < secret_number:
        print("To Low")
        attempts -= 1

    if attempts > 0:
        print(f"You have {attempts} attempts left")
    elif attempts == 0:
        print(lose)


