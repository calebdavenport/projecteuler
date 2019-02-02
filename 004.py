#!/usr/bin/python3

"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
Explanation:
Starting from 999 * 999, it would not be wise to create nested for loops. This
would result in searches that would find results like 998 * 67 = 66866.

Instead, treat each pair of numbers as a sum. Find all the products of all
pairs of factors that add to 1998, then 1997, then 1996, then (...).
"""

import math

NUM = 999


def main():
    for i in range(NUM * 2)[::-1]:
        for j in range(math.ceil(i / 2), NUM + 1):
            if checkPalindrome(j*(i-j)):
                print(j*(i-j))
                return


def checkPalindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == "__main__":
    main()
