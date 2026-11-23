def reverse_number(n):
    is_negative = n < 0
    number = abs(n)
    result = 0
    while number > 0:
        digit = number % 10
        result = (result * 10) + digit
        number //= 10
    
    return - result if is_negative else result

def is_number_palindrome(n):
    if n < 0:
        return False
    return n == reverse_number(n)



assert is_number_palindrome(-121) == False
assert is_number_palindrome(121) == True
assert is_number_palindrome(1331) == True
assert is_number_palindrome(123) == False
assert is_number_palindrome(7) == True
assert is_number_palindrome(120) == False

assert reverse_number(1234) == 4321
assert reverse_number(7) == 7
assert reverse_number(0) == 0
assert reverse_number(120) == 21
assert reverse_number(-123) == -321