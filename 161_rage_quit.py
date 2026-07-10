single_string = input()
rage_message = ""
sub_string = ""
repetitions = ""

for index in range(len(single_string)):
    if not single_string[index].isdigit():
        sub_string += single_string[index].upper()
    else:
        repetitions += single_string[index]
        if index +1 < len(single_string):
            if single_string[index+1].isdigit():
                repetitions += single_string[index+1]
        rage_message += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)