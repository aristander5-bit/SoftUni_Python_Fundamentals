number_of_symbols = int(input())

for symbol_1 in range(97, 97 + number_of_symbols):
    for symbol_2 in range(97, 97 + number_of_symbols):
        for symbol_3 in range(97, 97 + number_of_symbols):
            print(f"{chr(symbol_1)}{chr(symbol_2)}{chr(symbol_3)}")