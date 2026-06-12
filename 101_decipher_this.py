messages = input().split()
deciphered_message = []

for message in messages:
    message = list(message)
    digits_as_string = ""
    for index in range(len(message)):
        if message[index].isdigit():
            digits_as_string += message[index]
        else:
            break
    first_letter = chr(int(digits_as_string))
    message = [first_letter] + message[index:]
    message[1], message[-1] = message[-1], message[1]
    deciphered_message.append("".join(message))
print(" ".join(deciphered_message))