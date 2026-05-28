gifts = input().split()

while True:
    command_input = input()
    if command_input == "No Money":
        break

    command_parts = command_input.split()
    action = command_parts[0]

    if action == "OutOfStock":
        gift_to_remove = command_parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"

    elif action == "Required":
        gift_to_replace = command_parts[1]
        index = int(command_parts[2])

        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace

    elif action == "JustInCase":
        new_gift = command_parts[1]
        gifts[-1] = new_gift

final_gifts = []
for gift in gifts:
    if gift != "None":
        final_gifts.append(gift)

print(" ".join(final_gifts))