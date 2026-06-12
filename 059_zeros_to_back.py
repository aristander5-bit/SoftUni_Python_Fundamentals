single_string = input().split(", ")

others = []
zero = []

for num_as_string in single_string:
    num = int(num_as_string)

    if num == 0:
        zero.append(num)
    else:
        others.append(num)

final_list = others + zero

print(final_list)
