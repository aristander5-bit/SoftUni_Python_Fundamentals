fires_input = input().split('#')
water = int(input())

extinguished_cells = []
total_effort = 0.0

for fire in fires_input:
    fire_parts = fire.split(' = ')
    type_of_fire = fire_parts[0]
    cell_value = int(fire_parts[1])

    is_valid = False
    if type_of_fire == "High" and 81 <= cell_value <= 125:
        is_valid = True
    elif type_of_fire == "Medium" and 51 <= cell_value <= 80:
        is_valid = True
    elif type_of_fire == "Low" and 1 <= cell_value <= 50:
        is_valid = True

    if is_valid and water >= cell_value:
        water -= cell_value
        total_effort += cell_value * 0.25
        extinguished_cells.append(cell_value)

print("Cells:")
for cell in extinguished_cells:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")

total_fire = sum(extinguished_cells)
print(f"Total Fire: {total_fire}")