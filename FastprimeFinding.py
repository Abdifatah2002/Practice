"""Faster Prime Finding
Write a function that returns a list of all primes up to a given number.
For each number, in order to determine if it is prime, take the following steps:
Find the square root of the number
Find all the primes up to that square root
Test to see if any of those primes are divisors
If a number has no prime divisors, it is prime!
"""

def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = int(number ** 0.5)  # Correct the square root calculation

        for factor in primes:
            if number % factor == 0:
                # Not prime
                break  # Exit the loop if not prime

            if factor > sqrtNum:
                # It's prime
                primes.append(number)
                break  # Exit the loop after appending the prime number

    return primes


