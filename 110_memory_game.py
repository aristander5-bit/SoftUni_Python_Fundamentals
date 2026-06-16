elements = input().split()
numbers_of_moves_until_now = 0
player_won_the_game = False
command = input()
while command != "end":
    numbers_of_moves_until_now += 1
    command_as_list = command.split()
    first_index = int(command_as_list[0])
    second_index = int(command_as_list[1])
    if first_index == second_index \
            or first_index not in range(len(elements)) \
        or second_index not in range(len(elements)):
        middle_of_elements = len(elements) // 2
        first_part = elements[:middle_of_elements]
        second_part = elements[middle_of_elements:]
        elements = first_part + \
                   [f"-{numbers_of_moves_until_now}a", f"-{numbers_of_moves_until_now}a"] + \
                   second_part
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[first_index] == elements[second_index]:
            matched_element = elements[first_index]
            while matched_element in elements:
                elements.remove(matched_element)
            print(f"Congrats! You have found matching elements - {matched_element}!")
        else:
            print("Try again!")
    if not elements: # if len(elements) == 0:
        player_won_the_game = True
        break
    command = input()
if player_won_the_game: # if player_won_the_game == True:
    print(f"You have won in {numbers_of_moves_until_now} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))



