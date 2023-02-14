import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [number for number in numbers if is_prime(number)]

numbers =[int(i) for i in input().split()]
print(filter_prime(numbers))