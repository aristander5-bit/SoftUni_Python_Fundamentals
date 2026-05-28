
energy = 100
coins = 100

events = input().split('|')

day_completed = True

for event in events:
    event_parts = event.split('-')
    event_name = event_parts[0]
    value = int(event_parts[1])

    if event_name == "rest":

        gained_energy = value
        if energy + value > 100:
            gained_energy = 100 - energy

        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:

        ingredient = event_name
        if coins >= value:
            coins -= value
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")