
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
    print "Iterations: " + str(iterations)
    print "Length of numbers: " + str(length_of_numbers)
    print "Prime Numbers between 1 and " + str(max_prime) + ":"
    print numbers
    return numbers

findPrimes(100000)