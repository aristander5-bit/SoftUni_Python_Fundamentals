first_key = input().split()
keys = []

for key in first_key:
    keys.append(int(key))

while True:
    line = input()
    if line == "find":
        break

    decrypted_key = ""

    for index in range(len(line)):

        current_key = keys[index % len(keys)]
        decrypted_key += chr(ord(line[index]) - current_key)

    start_type = decrypted_key.index("&") + 1
    end_type = decrypted_key.index("&", start_type)
    treasure_type = decrypted_key[start_type:end_type]

    start_coords = decrypted_key.index("<") + 1
    end_coords = decrypted_key.index(">")
    coordinates = decrypted_key[start_coords:end_coords]

    print(f"Found {treasure_type} at {coordinates}")


