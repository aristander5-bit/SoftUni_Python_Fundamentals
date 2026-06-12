to_do_list = [0] * 10

while True:
    command = input()

    if command == 'End':
        break

    tokens = command.split('-')
    importance = int(tokens[0])
    note = tokens[1]

    index = importance - 1
    to_do_list.insert(index, note)
    to_do_list.pop(index + 1)

final_list = [task for task in to_do_list if task != 0]
print(final_list)
        