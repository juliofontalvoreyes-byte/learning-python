def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)


assert gcd(48, 18) == 6
assert gcd(17, 5) == 1
assert gcd(7, 7) == 7
assert gcd(5, 0) == 5
assert gcd(18, 48) == 6
assert lcm(4, 6) == 12
assert lcm(17, 5) == 85
assert lcm(0, 0) == 0
assert lcm(0, 5) == 0
assert lcm(7, 0) == 0