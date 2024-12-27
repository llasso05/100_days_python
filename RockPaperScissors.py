import random

print("""Welcome to Rock, Paper, Scissors!\n
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
                     
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     

          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \ -
|___/\___|_|___/___/\___/|_|  |___/

""")
rounds = int(input("How many rounds would you like to play?: "))
while rounds > 0:
    # game variables
    user_choice = input("Rock, Paper, or Scissors?('R','P','S') ")
    pc_choices = ['R', 'P', 'S']
    random_choice = random.choice(pc_choices)
    match_choices = []
    winner = ''

    # print(random_choice)
    # print(user_choice)
    # print(rounds)

    match_choices.append(random_choice)
    match_choices.append(user_choice)
    print(match_choices)

    # Winner selection
    if 'R' in match_choices and 'S' in match_choices:
        winner = 'R'
    elif 'R' in match_choices and 'P' in match_choices:
        winner = 'P'
    elif 'S' in match_choices and 'P' in match_choices:
        winner = 'S'
    elif match_choices[0] == match_choices[1]:
        print("It's a tie, try again")
        continue
    else:
        print("please pick between 'R', 'P', 'S'")

    # winner logic
    if winner == user_choice:
        print(f'{user_choice} beats {random_choice} you win')
    else:
        print(f'{random_choice} beats {user_choice} you lose')

    rounds -= 1




