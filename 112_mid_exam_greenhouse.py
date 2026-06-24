crops_string = input().split(" & ")
command = input()

while command != "Collect!":
    command_as_list = command.split()
    movement = command_as_list[0]

    if movement == "Plant":
        crop = command_as_list[1]
        if crop not in crops_string:
            crops_string.insert(0, crop)
    elif movement == "Transplant":
        crop = command_as_list[1]
        if crop in crops_string:
            crops_string.remove(crop)
            crops_string.append(crop)
    elif movement == "Replace":
        index_1 = int(command_as_list[1])
        index_2 = int(command_as_list[2])
        if 0 <= index_1 < len(crops_string) and 0 <= index_2 < len(crops_string):
            crops_string[index_1], crops_string[index_2] = crops_string[index_2], crops_string[index_1]
    elif movement == "Uproot":
        crop  = command_as_list[1]
        if crop in crops_string:
            crops_string.remove(crop)

    command = input()

print(" | ".join(crops_string))