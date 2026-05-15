current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        for symbol in current_string:
            print(symbol*2, end="")
        print()
    current_string = input()

