def is_even(current_number:int)->bool:

    return current_number % 2 == 0
numbers_as_string = input().split()
even_numbers = []
numbers_as_digit = []
for digit in numbers_as_string:
    digit_is_even = is_even(int(digit))
    if digit_is_even:
        even_numbers.append(int(digit))

print(even_numbers)