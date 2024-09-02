#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n using
    the Sieve of Eratosthenes algorithm."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):  # This should be `n ** 0.5`
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def isWinner(x, nums):
    """Determine the winner of each game round."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = 0
        for prime in primes:
            if prime <= n:
                primes_count += 1
            else:
                break
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
