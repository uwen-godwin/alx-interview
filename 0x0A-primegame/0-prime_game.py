#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Return a list of booleans representing primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def play_game(n, primes):
    """Simulate one round of the game and return the winner ("Maria" or "Ben")."""
    nums = list(range(1, n + 1))
    maria_turn = True  # Maria always starts
    while True:
        # Find the next prime number in the list
        prime_found = False
        for i in range(2, n + 1):
            if primes[i] and i in nums:
                prime_found = True
                # Remove the prime and all its multiples
                nums = [num for num in nums if num % i != 0]
                break

        if not prime_found:
            # No more primes left, current player loses
            return "Maria" if not maria_turn else "Ben"

        # Alternate turns
        maria_turn = not maria_turn


def isWinner(x, nums):
    """Determine the overall winner after x rounds."""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
