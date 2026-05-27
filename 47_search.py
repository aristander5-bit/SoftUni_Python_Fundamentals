n = int(input())
magic_word = input()

strings = []

for i in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []
for string in strings:
    if magic_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)