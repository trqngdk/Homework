"""
perf_counter() is imported so that timing information
can be collected on how long this program took to
execute without memoization enabled versus when
memoization was enabled for comparison purposes later.
"""
from time import perf_counter
from functools import wraps


def memoize(func):
    """
    Creates a function called memoize which takes in
    a function as an argument.The wrapper method is used to create
    an anonymous function which has access to all of the arguments.
    It then stores this new anonymous function in the cache dictionary,
    and returns it for later use. The code above calculates how long
    it would take for the program without memoization enabled
    versus when memoization was enabled for comparison purposes later on.
    """

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
            return cache[key]
    return wrapper


@memoize
def sieve_prime_number():
    """
    Calculates how long it would take
    for a computer to calculate the sieve of Eratosthenes
    by calculating how long it would take for a computer
    to run through each prime number in order, and then
    iterating over them again with an updated list of primes.
    """

    # Store list of prime numbers.
    number = input().split()
    left_number = int(number[0])
    right_number = int(number[1])

    sieve = [0] * (right_number + 11)

    # Creates an empty list with 500 elements for each element in the range from 2-500.
    for k in range(2, 500):
        if k == right_number:
            break
        if sieve[k] == 0:
            number = k * k
            while number <= right_number:
                sieve[number] = 1
                number += k

    sieve[0] = sieve[1] = 1
    start = perf_counter()

    # Iterates through all integers between a and b+1.
    for k in range(left_number, right_number + 1):

        # If there is no prime number at its current iteration,
        # prints out the value of k where k is one less than or equal to b.
        if sieve[k] == 0:
            print(k)
    end = perf_counter()
    time = float(end - start)
    print("Time: ", time, " seconds")


sieve_prime_number()
