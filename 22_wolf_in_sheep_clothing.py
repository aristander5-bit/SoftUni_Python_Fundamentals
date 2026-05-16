text = input()

if text.endswith("wolf"):
    print("Please go away and stop eating my sheep")
else:
    sheep_count = 0

    for index in range(len(text) - 1, -1, -1):
        if text[index] == ",":
            sheep_count += 1
        if text[index] == "w":
            print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
            break