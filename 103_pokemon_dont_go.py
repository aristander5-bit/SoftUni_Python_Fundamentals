def update_sequence(sequence: list, removed_element:int) -> list:
    for index in range(len(sequence)):
        if sequence[index] <= removed_element:
            sequence[index] += removed_element
        else:
            sequence[index] -= removed_element

    return sequence

input_strings = input().strip().split()
pokemon = []
total_sum = 0

for i in input_strings:
    number = int(i)
    pokemon.append(number)

while len(pokemon) > 0:
    index = int(input())
    removed_pokemon = 0

    if index < 0:
        removed_pokemon = pokemon[0]
        last_element = pokemon[-1]
        pokemon.pop(0)
        pokemon.insert(0, last_element)
    elif index >= len(pokemon):
        removed_pokemon = pokemon[-1]
        first_element = pokemon[0]
        pokemon.pop()
        pokemon.append(first_element)
    else:
        removed_pokemon = pokemon.pop(index)

    total_sum += removed_pokemon
    pokemon = update_sequence(pokemon, removed_pokemon)

print(total_sum)