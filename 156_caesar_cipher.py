text = input()
encrypted_version = ""

for character in text:
     encrypted_symbol = chr(ord(character) + 3)
     encrypted_version += encrypted_symbol
print(encrypted_version)