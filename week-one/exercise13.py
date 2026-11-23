def fibonacci(n):
    if n < 0:
        return -1
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_even(n):
    return n % 2 == 0

def sum_even_fibonacci(limit):
    a, b = 0, 1
    result = 0
    while a <= limit:
        if is_even(a):
            result += a
        a, b = b, a + b
    return result

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(10) == 55
assert fibonacci(30) == 832040
assert fibonacci(-5) == -1

assert sum_even_fibonacci(10) == 10
assert sum_even_fibonacci(100) == 44
assert sum_even_fibonacci(4000000) == 4613732
assert sum_even_fibonacci(1) == 0
assert sum_even_fibonacci(-5) == 0