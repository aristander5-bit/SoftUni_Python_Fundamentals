def all_the_characters(first:str, second:str)-> list:
    characters = []
    for character_as_digit in range(ord(first) + 1, ord(second)):
        characters.append(chr(character_as_digit))

    return characters

first_character = input()
second_character = input()
result = all_the_characters(first_character, second_character)
print(" ".join(result))