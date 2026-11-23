def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def is_armstrong(n):
    if n < 0:
        return False

    digit_count = count_digits(n)
    number = n
    result = 0
    
    while number > 0:
        digit = number % 10
        result += digit ** digit_count
        number //= 10
    return n == result

for i in range(1, 100001):
    if is_armstrong(i):
        print(i)

assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(9474) == True
assert is_armstrong(100) == False
assert is_armstrong(10) == False
assert is_armstrong(5) == True
assert is_armstrong(-153) == False
