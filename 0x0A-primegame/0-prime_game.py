#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n using the Sieve of Eratosthenes algorithm."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def isWinner(x, nums):
    """Determine the winner of the most rounds."""
    if not nums or x < 1:
        return None
    
    # Find the maximum number in nums to determine the sieve limit
    max_num = max(nums)
    
    # Precompute all prime numbers up to the largest number in nums
    primes = sieve_of_eratosthenes(max_num)
    
    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        primes_count = sum(1 for prime in primes if prime <= n)
        
        # Maria wins if the count of primes is odd, Ben wins if even
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
