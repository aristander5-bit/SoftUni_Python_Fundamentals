cards_string = input().split(", ")
commands_count = int(input())

for i in range(commands_count):
    command_as_list = input().split(", ")
    movement = command_as_list[0]
    if movement == "Add":
        card_name = command_as_list[1]
        if card_name not in cards_string:
            cards_string.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif movement == "Remove":
        card_name = command_as_list[1]
        if card_name in cards_string:
            cards_string.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif movement == "Remove At":
        index = int(command_as_list[1])
        if index in range(len(cards_string)):
            cards_string.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif movement == "Insert":
        index = int(command_as_list[1])
        card_name = command_as_list[2]
        if index not in range (len(cards_string)):
            print("Index out of range")
        elif card_name in cards_string:
            print("Card is already added")
        else:
            cards_string.insert(index, card_name)
            print("Card successfully added")

print(", ".join(cards_string))

