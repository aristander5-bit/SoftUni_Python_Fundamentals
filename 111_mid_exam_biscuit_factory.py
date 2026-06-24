from math import floor

biscuit_per_day = int(input())
count_of_workers = int(input())
competing_factory_produced = int(input())

total_biscuits = 0

for day in range(1, 31):
    daily_product = biscuit_per_day * count_of_workers

    if day % 3 == 0:
        daily_product *= 0.75
    total_biscuits += floor(daily_product)

diff = abs(total_biscuits - competing_factory_produced)
percent_diff = (diff / competing_factory_produced) * 100

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competing_factory_produced:
    print(f"You produce {percent_diff:.2f} percent more biscuits.")
else:
    print(f"You produce {percent_diff:.2f} percent less biscuits.")

