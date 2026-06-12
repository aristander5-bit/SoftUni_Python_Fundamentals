string_one = input()
string_two = input()
previous_string = string_one

for index in range(len(string_one)):
    part_left = string_two[:index + 1]
    part_right = string_one[index + 1:]
    new_string = part_left + part_right

    if new_string == previous_string:
        continue
    print(new_string)

    previous_string = new_string