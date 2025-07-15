def is_prime(num):
    divisor = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = []
    # Removing self
    if num in divisor:
        divisor.remove(num)
        # print(divisor)
    # adding results to list
    for number in divisor:
        result.append(num % number)
        # print(result)
    # final check
    if 0 in result:
        return False
    else:
        return True


is_prime(7)
is_prime(73)
is_prime(75)

