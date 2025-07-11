print("""
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
    
  ___                            ___
 ||  |   ___         ___        ||  |
 || _|__/  _\_______/  _\_______|| _|
 ||(___(  (________(  (_________||((_)
 ||  |  \___/       \___/       ||  |
 ||  |         ___              ||  |
 || _|________/  _\_____________|| _|
 ||(_________(  (_______________||((_)
 ||  |        \___/             ||  |
 ||  |                          ||  |
 ||  |                          ||  |
 ||  |                          ||  |
                            """
)

def add(n1, n2):
    return n1 + n2

# TODO: Write aout the other 3 functions - subtract, multiply, and divide.
def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = int(input("Please input your number here: "))
another_calculation = "yes"

while another_calculation == "yes":
    for symbol in operations:
        print(symbol)
    operation = input("Please select your opeartion: ")
    second_number = int(input("Please select your second number: "))
    first_number = operations[operation](first_number, second_number)
    print(first_number)
    another_calculation = input("Do you want to do another calculation: (Yes/No) ").lower()
