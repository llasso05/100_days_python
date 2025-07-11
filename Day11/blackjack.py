import random

print("""
                      ______________________________________
                     /   _______________________________    \
                    |   |            __ __              |   |
                    | _ |    /\     ) _) /''''',        |   |
                    |(.)|   <  >    \ ) // '  `,        |   |
                    | ` |    \/       \/// ~ |~:    +   |   |
                    |   |             ///*\  ' :    |   |   |
                    |   |            ///***\_~.'    |   |   |
                    |   |  .'.    __///````,,..\_   |   |   |
                    |   |   ` \ _/* +_\#\\~\ooo/ \  |   |   |
                    |   |     |/:\ + *\_\#\~\so/!!\ |   |   |
                    |   |    _\_::\ * + \-\#\\o/!!!\|   |   |
                    |   |   / <_=::\ + */_____@_!!!_|   |   |
                    |   |  <__/_____\ */( /\______ _|   |   |
                    |   |   |_   _ __\/_)/* \   ._/  >  |   |
                    |   |   | !!! @     /* + \::=_>_/   |   |
                    |   |   |\!!!/o\\#\_\ + * \::_\     |   |
                    |   |   | \!!/os\~\#_\_* + \:/|     |   |
                    |   |   |  \_/ooo\~\\#_\+_*/- \     |   |
                    |   |   |    \''``,,,,///      .`.  |   |
                    |   |   |     ,.- ***///        '   |   |
                    |   |   |    : ~  \*///             |   |
                    |   |   +    : |   \//\             |   |
                    |   |        ,~  ~ //_( \     /\    | ; |
                    |   |        ,'  ` /_(__(    <  >   |(_)|
                    |   |         `````           \/    |   |
                    |   |_______________________________|   |
                     \______________________________________/
                 __
                /  >
  *            /  /________________________________________________
 (O)77777777777)  7                                                `~~--__
8OO>>>>>>>>>>>>] <===   Blackjack           __-
 (O)LLLLLLLLLLL)  L________________________________________________.--~~
  *            \  \
                \__>
    
""")

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

new_game = "yes"



# def calculation(hand, total):
#     for card in hand:
#         total += values[card]


def draw_card(player):
    player.append(cards[random.randint(0, 13)-1])
    # print(f'New hand {player}')


def hand_calculation(current_hand, current_total):
    for card in current_hand:
        current_total += values[card]
    if "A" in current_hand and current_total > 21:
        current_total -= 10
    return current_total


# game variables
player_hand = []
player_total = 0
cpu_hand = []
cpu_total = 0
additional_draw = ""

# game loop
while new_game == "yes":
    player_hand = []
    player_total = 0
    cpu_hand = []
    cpu_total = 0

    # first draw
    for i in range(2):
        draw_card(cpu_hand)
        draw_card(player_hand)

    # first hand
    hidden_card = cpu_hand[1]
    print(f"This is your draw {player_hand}")
    print(f"This is the house draw [*, {hidden_card}]")

    # additional draw
    additional_draw = "yes"
    while additional_draw != "no":
        additional_draw = input("Do you want to draw another cards?: (yes/no) ").lower()
        if additional_draw == "yes":
            draw_card(player_hand)
            print(f"This is your draw {player_hand}")

        if hand_calculation(player_hand, player_total) > 21:
            print("You Lose")
            break
        elif hand_calculation(player_hand, player_total) == 21:
            print("Black-Jack! You Win!")
            break

    # first calculation
    player_total = hand_calculation(player_hand, player_total)
    cpu_total = hand_calculation(cpu_hand, cpu_total)

    if player_total == 21:
        print("Black-Jack! You Win!")
    elif cpu_total == 21:
        print("House Wins! Black-Jack!")
    elif player_total % 21 > cpu_total % 21:
        print(f"You win! total: {player_total}, house total: {cpu_total} ")
    else:
        print(f"You lose! total: {player_total}, house total: {cpu_total} ")

    new_game = input("Do you want to play again?: (yes/no) ").lower()
