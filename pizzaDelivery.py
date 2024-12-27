

# todo: work out how much they need to pay based on their size choice
# small 15, medium 20, large 25
# todo: work out how much to add to their bill based on their pepperoni choice.
# add 2 for small and 3 for large or medium, add 1 for extra chesse
# todo: work out their final amount based on whether if they want extra cheese.


print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_chesse = input("Do you want extra cheese? Y or N:")
final_bill = 0

if size == "S":
    final_bill += 15
    if pepperoni == "Y":
        final_bill += 2
    if extra_chesse == "Y":
        final_bill += 1
elif size == "M":
    final_bill += 20
    if pepperoni == "Y":
        final_bill += 3
    if extra_chesse == "Y":
        final_bill += 1
elif size == "L":
    final_bill += 25
    if pepperoni == "Y":
        final_bill += 3
    if extra_chesse == "Y":
        final_bill += 1

print(f"Your final bill is: {final_bill}")





