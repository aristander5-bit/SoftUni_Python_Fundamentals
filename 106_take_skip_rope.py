input_string = input().strip()
numbers = []
no_numbers = []

for symbol in input_string:
    if symbol.isdigit():
        numbers.append(int(symbol))
    else:
        no_numbers.append(symbol)

take_list = []
skip_list = []

for number in range(len(numbers)):
    if number % 2 ==0:
        take_list.append(numbers[number])
    else:
        skip_list.append(numbers[number])

result_string = ""
current_number = 0
for number in range(len(take_list)):
    take_number = take_list[number]
    skip_number = skip_list[number]

    taken_part = no_numbers[current_number: current_number + take_number]
    result_string += "".join(taken_part)

    current_number += take_number
    current_number += skip_number

print(result_string)

