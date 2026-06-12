name = input()


while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    count = 0
    for char in name:
        count += 1

    if count < 5:
        print(f"{name} goes to Gryffindor.")
    elif count == 5:
        print(f"{name} goes to Slytherin.")
    elif count == 6:
        print(f"{name} goes to Ravenclaw.")
    elif count > 6:
        print(f"{name} goes to Hufflepuff.")

    name = input()
else:
    print("Welcome to Hogwarts.")