budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
price_needed_milk_250 = price_milk / 4

bread_price = price_flour + price_eggs + price_needed_milk_250

count_bread = 0
count_eggs = 0

while budget >= bread_price:
    budget -= bread_price
    count_bread += 1
    count_eggs += 3

    if count_bread % 3 == 0:
        lost_eggs = count_bread - 2
        count_eggs -= lost_eggs
print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")




