number_of_cars = int(input())
cars = {}

for data in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()
while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]

    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        current_fuel = cars[car]["fuel"]
        if current_fuel + fuel > 75:
            fuel_added = 75 - current_fuel
            cars[car]["fuel"] = 75
        else:
            fuel_added = fuel
            cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel_added} liters")
    elif action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, car_data in cars.items():
    mileage = car_data["mileage"]
    fuel = car_data["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")