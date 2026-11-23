def to_binary(n):
    if n < 0:
        return -1
    divisor = 2
    binary = 0
    index_count = 1

    while n != 0:
        bit = n % divisor
        binary += bit * index_count 
        index_count *= 10
        n //= divisor
    return binary


def from_binary(binary):

    if binary < 0:
        return -1

    num = 0
    position = 1

    while binary > 0:
        digit = binary % 10
        num += position * digit
        position *= 2
        binary //= 10
    return num

for i in range(1000):
    assert from_binary(to_binary(i)) == i

assert to_binary(0) == 0
assert to_binary(1) == 1
assert to_binary(2) == 10
assert to_binary(5) == 101
assert to_binary(13) == 1101
assert to_binary(255) == 11111111
assert to_binary(-5) == -1

assert from_binary(0) == 0
assert from_binary(101) == 5
assert from_binary(1101) == 13
assert from_binary(11111111) == 255
assert from_binary(-5) == -1