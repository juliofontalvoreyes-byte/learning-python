def sum_divisors(number):
    result = 0
    for i in range(1, int(number ** 0.5 ) + 1):
        if number % i == 0:
            result += i
            if i != number // i:
                result += number // i
    return result - number

def is_perfect(n):
    if n <= 0:
        return False
    return n == sum_divisors(n)

for i in range(1, 100001):
    if is_perfect(i):
        print(i)

assert sum_divisors(6) == 6
assert sum_divisors(8) == 7
assert sum_divisors(12) == 16
assert sum_divisors(1) == 0
assert is_perfect(6) == True
assert is_perfect(28) == True
assert is_perfect(12) == False
assert is_perfect(1) == False
assert is_perfect(0) == False
assert is_perfect(-6) == False
assert sum_divisors(36) == 55
