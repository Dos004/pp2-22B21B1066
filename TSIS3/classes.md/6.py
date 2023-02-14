# define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# define a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# use the filter function to filter out non-prime numbers
primes = list(filter(lambda x: is_prime(x), numbers))

# print the filtered list of prime numbers
print(primes)  # is should output [2, 3, 5, 7]