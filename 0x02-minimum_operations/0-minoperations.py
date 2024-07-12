#!/usr/bin/python3
"""
This module contains a function to calculate the
minimum number of operations
needed to achieve exactly n H characters in
a text file starting with a single H.
"""


def minOperations(n):
    """
    Calculate the fewest number of
    operations needed to result in exactly n H characters.

    :param n: int, the target number of H characters
    :return: int, the minimum number of operations needed or 0 if impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
