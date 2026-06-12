def is_even(current_number:int)->bool:
    # if current_number % 2 == 0:
    #     return True
    # return False
    return current_number % 2 == 0
numbers_as_string = input().split()
numbers_as_digit = []
for number in numbers_as_string:
    numbers_as_digit.append(int(number))
result = list(filter(is_even, numbers_as_digit))
print(result)