#!/usr/bin/python3
"""
The challenge involves determining the winner of a game based on the
strategic removal of prime numbers and their multiples
from a set of consecutive integers.
"""


def isWinner(x, nums):
    """Finds who the winner is
    """
    # Edge case: if no rounds or nums is empty, return None
    if not nums or x < 1:
        return None

    # Step 1: Precompute primes up to the largest n using Sieve of Eratosthenes
    max_num = max(nums)  # Largest n from the input
    # Create a boolean array for primality check
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False  # Mark multiples of i as non-prime

    # Step 2: Function to simulate a round and determine the winner
    def play_game(n):
        """
        Simulates a game round and returns 0 for Maria's win, 1 for Ben's win.
        """
        prime_count = sum(primes[2:n+1])  # Count of primes from 2 to n
        # Maria wins if the prime count is odd (she plays first)
        # Ben wins if the prime count is even
        return 0 if prime_count % 2 != 0 else 1

    # Step 3: Tally wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n) == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
