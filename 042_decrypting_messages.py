key = int(input())
num_lines = int(input())

message = ""

for i in range(num_lines):
    letter = input()

    decrypted = chr(ord(letter)+ key)

    message += decrypted

print(message)
