single_string = input()
final_string = ""
strength = 0

for index in range(len(single_string)):
    if single_string[index] == ">":
        final_string += ">"
        strength += int(single_string[index+1])
    elif strength > 0 and single_string[index] != ">":
        strength -= 1
    else:
        final_string += single_string[index]

print(final_string)