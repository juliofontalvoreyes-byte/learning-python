def is_even(n):
    return n % 2 == 0

def collatz_steps(n):
    if n <= 0:
        return -1
    
    count = 0

    while n != 1:
        if is_even(n):
            n //= 2
        else:
            n = (n * 3) + 1

        count += 1
    return count

def longest_collatz(limit):
    max_steps = -1
    best_number = 0
    for i in range(1, limit + 1):
        steps = collatz_steps(i)
        if max_steps < steps:
            max_steps = steps
            best_number = i
    return best_number, max_steps

number, steps = longest_collatz(1)
print(f"The number {number} takes {steps} steps")

assert longest_collatz(1000) == (871, 178)
assert longest_collatz(1) == (1, 0)

assert collatz_steps(6) == 8
assert collatz_steps(1) == 0
assert collatz_steps(2) == 1
assert collatz_steps(7) == 16
assert collatz_steps(27) == 111
assert collatz_steps(0) == -1
assert collatz_steps(-5) == -1