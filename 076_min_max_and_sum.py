def sequence_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)

    return minimum, maximum, total_sum

input_numbers = input().split()
cleared_numbers = []

for i in input_numbers:
    number = int(i)
    cleared_numbers.append(number)

min_number, max_number, total = sequence_numbers(cleared_numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {total}")


