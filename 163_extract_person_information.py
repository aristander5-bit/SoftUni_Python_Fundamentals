num_string = int(input())

for index in range(num_string):
    line = input()
    name = ""
    age = ""

    is_name = False
    is_age = False

    for character in line:
        if character == "@":
            is_name = True
            continue
        elif character == "|":
            is_name = False

        if character == "#":
            is_age = True
            continue
        elif character == "*":
            is_age = False

        if is_name:
            name += character
        elif is_age:
            age += character

    print(f"{name} is {age} years old.")





