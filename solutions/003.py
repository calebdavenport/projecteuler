#!/usr/bin/python3

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Explanation:
All the factors of a number must exist inside the range of 2 to sqrt(num).

Once a factor is found, the function is ran again with number / factor. When
the for loop completes without any breaks, the last number must be the largest
prime factor.
"""

import math

NUM = 600851475143


def main():
    print(largestFactor(NUM))


def largestFactor(composite, factor=2):
    for i in range(factor, int(math.floor(math.sqrt(composite))) + 1):
        if composite % i == 0:
            return largestFactor(composite // i, factor)
    else:
        return composite


if __name__ == "__main__":
    main()
