input_numbers = input().split()
rounded_numbers = []

for number in input_numbers:
    num_float = float(number)

    num_rounded = round(num_float)
    rounded_numbers.append(num_rounded)
print(rounded_numbers)