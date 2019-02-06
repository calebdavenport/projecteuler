#!/usr/bin/python3

"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

NUM = 100


def main():
    print(squareOfSums(NUM) - sumOfSquares(NUM))


def sumOfSquares(n):
    total = 0
    for i in range(n + 1):
        total += i**2
    return total


def squareOfSums(n):
    return ((n + 1) * (n // 2))**2


if __name__ == "__main__":
    main()
