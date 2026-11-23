def count_prime_factors(n):
    if n < 1:
        return -1
    
    count_factors = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            n //= divisor
            count_factors += 1
        divisor += 1
    if n > 1:
        count_factors += 1
    return count_factors

def largest_prime_factor(n):
    if n < 1:
        return -1

    largest_factor = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            n //= divisor
            largest_factor = divisor
        divisor += 1
    if n > 1:
        return n
    return largest_factor

assert largest_prime_factor(12) == 3
assert largest_prime_factor(360) == 5
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(7) == 7
assert largest_prime_factor(600851475143) == 6857
assert largest_prime_factor(1000000007) == 1000000007
assert largest_prime_factor(4) == 2
assert largest_prime_factor(36) == 3
assert largest_prime_factor(1) == 0
assert largest_prime_factor(0) == -1


assert count_prime_factors(12) == 3
assert count_prime_factors(360) == 6
assert count_prime_factors(7) == 1
assert count_prime_factors(2) == 1
assert count_prime_factors(1) == 0
assert count_prime_factors(0) == -1
assert count_prime_factors(-12) == -1
assert count_prime_factors(1000000007) == 1
assert count_prime_factors(36) == 4
assert count_prime_factors(600851475143) == 4
