numbers = input().split()
text = input()

message = []

for num in numbers:
    digit_sum = 0
    for char in num:
        digit_sum += int(char)

    current_len = len(text)

    valid_index = digit_sum % current_len

    char_found = text[valid_index]
    message.append(char_found)

    text = text[:valid_index] + text[valid_index+1:]

print(''.join(message))