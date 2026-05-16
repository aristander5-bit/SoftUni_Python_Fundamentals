text = input()
capital_indices = []

for index in range(len(text)):
    current = text[index]

    if current.isupper():
        capital_indices.append(index)

print(capital_indices)

