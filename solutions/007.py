#!/usr/bin/python3

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

NUM = 10001


def main():
    primes = []
    n = 1
    while len(primes) < NUM:
        n += 1
        if isPrime(n):
            primes.append(n)
    print(primes[-1])


def isPrime(composite):
    for i in range(2, int(math.floor(math.sqrt(composite))) + 1):
        if composite % i == 0:
            return False
    else:
        return True


if __name__ == "__main__":
    main()
