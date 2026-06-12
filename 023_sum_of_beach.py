text = input().lower()
count = 0

for index in range(len(text)):
    if text[index: index + 3] == "sun":
        count += 1
    if text[index: index + 4] == "sand" or \
        text[index: index + 4] == "fish":
        count += 1
    if text[index: index + 5] == "water":
        count += 1

print(count)