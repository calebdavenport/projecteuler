#!/usr/bin/python3

"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

import math

NUM = 23123


def main():
    abundantList = getAbundantList()
    remainingSums = [(_ + 1) for _ in range(NUM)]
    abundantSums = []

    for index, i in enumerate(abundantList):
        for j in abundantList[index:]:
            remove = i + j
            if remove > NUM:
                break
            abundantSums.append(remove)

    abundantSums = list(set(abundantSums))
    for i in abundantSums:
        remainingSums.remove(i)
    print(sum(remainingSums))


def getAbundantList():
    abundantSumList = []
    for n in range(1, NUM):
        abundantCheck = sum(getFactorList(n)) - n + 1
        if abundantCheck > n:
            abundantSumList.append(n)
    return abundantSumList


def getFactorList(composite, factorList=None):
    if factorList is None:
        factorList = []
    for i in range(2, int(math.floor(math.sqrt(composite))) + 1):
        if composite % i == 0:
            factorList.append(i)
            factorList.append(composite // i)
    else:
        factorList.append(composite)
        return list(set(factorList))


if __name__ == "__main__":
    main()
