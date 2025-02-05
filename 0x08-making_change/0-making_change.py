#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    :param coins: List of integers representing the coin denominations.
    :param total: Integer representing the total amount.
    :return: Fewest number of coins needed to meet total, or -1 if it
             cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins needed for each
    # amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
