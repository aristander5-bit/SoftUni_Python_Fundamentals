groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command_as_list = command.split()
    action = command_as_list[0]
    if action == "Urgent":
        item = command_as_list[1]
        if item not in groceries:
            groceries = [item] + groceries
    elif action == "Unnecessary":
        item = command_as_list[1]
        if item in groceries:
            groceries.remove(item)
    elif action == "Correct":
        old_item = command_as_list[1]
        new_item = command_as_list[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item
    elif action == "Rearrange":
        item = command_as_list[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    command = input()

print(", ".join(groceries))
