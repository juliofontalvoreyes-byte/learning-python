def count_digits(n):
    count = 0
    number = abs(n)  # Convert to absolute value to handle negative numbers
    if number == 0:
        return 1
    
    while number > 0:
        number //= 10
        count += 1
    return count

def sum_digits(n):
    number = abs(n)  # Convert to absolute value to handle negative numbers
    result = 0

    while number > 0:
        result += number % 10
        number //= 10
    return result

def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
number = get_number()
number_of_digits = count_digits(number)
print(f"The number {number} has {number_of_digits} {'digit' if number_of_digits == 1 else 'digits'}.")
print(f"The sum of the {'digit' if number_of_digits == 1 else 'digits'} of the number {number} is {sum_digits(number)}.")