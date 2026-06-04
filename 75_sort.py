input_data = input().split()
numbers_list = []
for number in input_data:
    numbers_list.append(int(number))

sorted_numbers_list = sorted(numbers_list)
print(sorted_numbers_list)