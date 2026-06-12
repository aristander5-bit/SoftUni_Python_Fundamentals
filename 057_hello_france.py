
items_input = input().split('|')
budget = float(input())

start_budget = budget

bought_items_new_prices = []

for item in items_input:
    item_parts = item.split('->')
    item_type = item_parts[0]
    item_price = float(item_parts[1])

    is_valid_item = False
    if item_type == "Clothes" and item_price <= 50.00:
        is_valid_item = True
    elif item_type == "Shoes" and item_price <= 35.00:
        is_valid_item = True
    elif item_type == "Accessories" and item_price <= 20.50:
        is_valid_item = True

    if is_valid_item and budget >= item_price:
        budget -= item_price

        new_price = item_price * 1.40
        bought_items_new_prices.append(new_price)

total_money_after_sales = budget + sum(bought_items_new_prices)

profit = total_money_after_sales - start_budget

formatted_prices = [f"{price:.2f}" for price in bought_items_new_prices]
print(" ".join(formatted_prices))

print(f"Profit: {profit:.2f}")

if total_money_after_sales >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")