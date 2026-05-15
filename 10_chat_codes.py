number_of_messages = int(input())

for message in range(number_of_messages):
    current_number = int(input())
    if current_number == 88:
        print(f"Hello")
    elif current_number == 86:
        print(f"How are you?")
    elif current_number < 88:
        print("GREAT!")
    elif current_number > 88:
        print(f"Bye.")