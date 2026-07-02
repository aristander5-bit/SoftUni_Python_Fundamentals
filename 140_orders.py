product_prices = {}
product_quantities = {}

while True:
    line = input()
    if line == "buy":
        break
    data = line.split()
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])

    product_prices[name] = price

    if name not in product_quantities:
        product_quantities[name] = quantity
    else:
        product_quantities[name] += quantity
for name in product_prices.keys():

    total_price = product_prices[name] * product_quantities[name]

    print(f"{name} -> {total_price:.2f}")