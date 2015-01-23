import numpy as np
def findPrimes(max_prime):
    """ This function returns the primes between 0 and max.

    This is based on the 'Sieve of Eratosthenes', which is a very common way
    of thinking about primes.

    Args:
        max_prime (int): The upper range of searching for primes.

    Returns:
        list: The number of primes in the range of 0 to max.
    """
    
    current_prime = 3
    numbers = range(1, max_prime + 1, 2)
    numbers[0] = 2
    find_new_prime = True

    iterations = 0
    length_of_numbers = []

    while (find_new_prime):
        iterations += 1
        find_new_prime = False

        num_iters = max_prime / current_prime + 1
        for iter_idx in range(2, num_iters + 1):
            if current_prime * iter_idx in numbers:
                numbers.remove(current_prime * iter_idx)

        # Get the index of the current prime
        idx = numbers.index(current_prime)
        if idx < len(numbers) - 1:
            find_new_prime = True
            current_prime = numbers[idx + 1]

        if len(length_of_numbers) > 0 and len(numbers) == length_of_numbers[-1]:
            break
        else:
            length_of_numbers.append(len(numbers))
    return numbers

# Code below from http://rosettacode.org/wiki/Lucas-Lehmer_test#Python
def isqrt(n):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        a = 1 << ((1 + n.bit_length()) >> 1)
        while True:
            b = (a + n // a) >> 1
            if b >= a:
                return a
            a = b
 
def isprime(n):
    if n < 5:
        return n == 2 or n == 3
    elif n%2 == 0:
        return False
    else:
        r = isqrt(n)
        k = 3
        while k <= r:
            if n%k == 0:
                return False
            k += 2
        return True
 
def lucas_lehmer_fast(n):
    if n == 2:
        return True
    elif not isprime(n):
        return False
    else:
        m = 2**n - 1
        s = 4
        for i in range(2, n):
            sqr = s*s
            r = (sqr & m) + (sqr >> n)
            if r >= m:
                r -= m
            s = r - 2
        return s == 0
# Code above is taken from http://rosettacode.org/wiki/Lucas-Lehmer_test#Python

