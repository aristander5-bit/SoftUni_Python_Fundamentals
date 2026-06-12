coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

def calculate_total(product, quantity):
    total = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return price * quantity
current_product = input()
current_quantity = int(input())

total_price = calculate_total(current_product, current_quantity)

print(f"{total_price:.2f}")
