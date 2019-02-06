#!/usr/bin/python3

"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

"""
Explanation:
Iterate through all the number 1 ... 20. If the number is a factor in the
current total, continue to the next number. If it is not a factor, multiply
the current total by all the prime factors that are currently not one of the
prime factors in the total.
"""

import math

NUM = 20


def main():
    total = 1
    for i in range(1, NUM + 1):
        if total % i == 0:
            continue
        for factor in getFactorList(i):
            if total % factor == 0:
                total = total // factor
        total *= i
    print(total)


def getFactorList(composite, factorList=None):
    if factorList is None:
        factorList = []
    for i in range(2, int(math.floor(math.sqrt(composite))) + 1):
        if composite % i == 0:
            factorList.append(i)
            return getFactorList(composite // i, factorList)
    else:
        factorList.append(composite)
        return factorList


if __name__ == "__main__":
    main()
