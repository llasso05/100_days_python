print(
"""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
"""
)
print("Welcome to the secret auction program!")
bids = {}
participants = "yes"

while participants == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid: "))
    bids[name] = bid
    print(bids)
    participants = input("Are there any other bidders?: Type 'yes' or 'no' ")
    if participants == "yes":
        print("\n" * 100)
    elif participants == "no":
        winner = max(bids, key=bids.get)
        winner_bid = max(bids.values())
        print(f"Winner: {winner}, bid {winner_bid}")

