def merge(data_list: list, start_index: int, end_index: int) -> list:
    if start_index < 0:
        start_index = 0
    if end_index >= len(data_list):
        end_index = len(data_list) - 1

    if start_index >= end_index:
        return data_list

    merged_string = "".join(data_list[start_index:end_index + 1])
    data_list[start_index:end_index + 1] = [merged_string]

    return data_list

def divide(data_list: list, index: int, partitions: int) -> list:
    element_to_divide = data_list[index]

    part_length = len(element_to_divide) // partitions

    new_parts = []
    current_index = 0

    for i in range(partitions - 1):
        next_part = element_to_divide[current_index:current_index + part_length]
        new_parts.append(next_part)
        current_index += part_length

    last_part = element_to_divide[current_index:]
    new_parts.append(last_part)
    data_list[index:index + 1] = new_parts

    return data_list

data = input().split()

while True:
    command_input = input()
    if command_input == "3:1":
        break

    tokens = command_input.split()
    action = tokens[0]

    if action == "merge":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        data = merge(data, start_index, end_index)

    elif action == "divide":
        index = int(tokens[1])
        parts = int(tokens[2])
        data = divide(data, index, parts)

print(*data)