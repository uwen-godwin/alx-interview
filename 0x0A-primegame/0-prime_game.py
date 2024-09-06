#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n using the
    Sieve of Eratosthenes algorithm.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def isWinner(x, nums):
    """
    Determines the winner of a game between Maria and Ben.

    Parameters:
    - x (int): The number of rounds.
    - nums (list): Array containing the upper limit n for each round.

    Returns:
    - The name of the player that won the most rounds ("Maria" or "Ben").
      If the result is a tie or no game is played, return None.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to calculate primes up to that number
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    # For each round, determine who wins based on the number of primes <= n
    for n in nums:
        primes_count = 0
        for prime in primes:
            if prime <= n:
                primes_count += 1
            else:
                break
        # Maria wins if the number of primes is odd, Ben wins if it's even
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
