budget = float(input())
price_flour_kg = float(input())

price_eggs = price_flour_kg * 0.75
price_milk = price_flour_kg * 1.25
price_milk_250_ml = price_milk / 4

bread_price = price_eggs + price_milk_250_ml + price_flour_kg

count_bread = 0
colored_eggs = 0

while budget >= bread_price:
    budget -= bread_price
    count_bread += 1
    colored_eggs += 3

    if count_bread % 3 == 0:
        lost_eggs = count_bread - 2
        colored_eggs -= lost_eggs
print(f"You made {count_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

