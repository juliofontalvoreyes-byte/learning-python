def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    result = 0

    while n > 0:
        digit = n % 10
        result = (result * 10) + digit
        n //= 10
    return result

def is_emirp(n):

    reverse_n = reverse_number(n)

    return is_prime(n) and is_prime(reverse_n) and reverse_n != n

def count_emirps(limit):
    count = 0

    for i in range(1, limit + 1):
        if is_emirp(i):
            count += 1
    return count

for i in range(1, 1001):
    if is_emirp(i):
        print(i)

assert is_prime(4) == False
assert is_prime(9) == False
assert is_prime(25) == False
assert is_prime(49) == False
assert is_prime(2) == True
assert is_prime(97) == True

assert is_emirp(13) == True
assert is_emirp(31) == True
assert is_emirp(107) == True
assert is_emirp(23) == False
assert is_emirp(11) == False
assert is_emirp(14) == False
assert is_emirp(2) == False
assert is_emirp(1) == False
assert is_emirp(0) == False
assert is_emirp(-13) == False

assert count_emirps(100) == 8
assert count_emirps(1000) == 36

