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
operation = input("Please select your opeartion: '*', '/', '+','-' ")
second_number = int(input("Please select your second number: "))

calculation = operations[operation](first_number, second_number)
print(calculation)