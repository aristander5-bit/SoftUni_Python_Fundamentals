stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

product_count = len(stock)
total_count = sum(stock.values())

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")