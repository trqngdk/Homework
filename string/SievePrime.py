from functools import wraps

# perf_counter() is imported so that timing information can be collected on how long this program took to
# execute without memoization enabled versus when memoization was enabled for comparison purposes later.
from time import perf_counter


# The code below creates a function called memoize which takes in a function as an argument.
# The wrapper method is used to create an anonymous function which has access to all of the arguments.
# It then stores this new anonymous function in the cache dictionary, and returns it for later use.
# The code above calculates how long it would take for the program without memoization enabled
# versus when memoization was enabled for comparison purposes later on.
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
            return cache[key]
    return wrapper


@memoize
# The code below calculates how long it would take for a computer to calculate the sieve of Eratosthenes
# by calculating how long it would take for a computer to run through each prime number in order,
# and then iterating over them again with an updated list of primes.
def sievePrimeNumber():

    # Store list of prime numbers
    n = input().split()
    a = int(n[0])
    b = int(n[1])

    sieve = [0] * (b + 11)

    # Creates an empty list with 500 elements for each element in the range from 2-500
    for k in range(2, 500):
        if k == b:
            break
        if sieve[k] == 0:
            n = k * k
            while n <= b:
                sieve[n] = 1
                n += k

    sieve[0] = sieve[1] = 1
    start = perf_counter()

    # Iterates through all integers between a and b+1
    for k in range(a, b + 1):

        # If there is no prime number at its current iteration, prints out the value of k where k is one less than or equal to b
        if sieve[k] == 0:
            print(k)
    end = perf_counter()
    time = float(end - start)
    print("Time: ", time, " seconds")


sievePrimeNumber()
