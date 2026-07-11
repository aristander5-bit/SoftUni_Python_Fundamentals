start_character = input()
end_character = input()
text = input()
total_sum = 0

lower_bound = min(ord(start_character), ord(end_character))
upper_bound = max(ord(start_character), ord(end_character))

for symbol in text:
    symbol_ascii = ord(symbol)

    if lower_bound < symbol_ascii < upper_bound:
        total_sum += symbol_ascii

print(total_sum)