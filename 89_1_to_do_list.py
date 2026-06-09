to_do_list = []

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-')
    importance = int(tokens[0])
    text = tokens[1]
    to_do_list.append((importance, text))

sorted_to_do_list = sorted(to_do_list, key=lambda x: x[0])
final_to_do_list = [i[1] for i in sorted_to_do_list]
print(final_to_do_list)
