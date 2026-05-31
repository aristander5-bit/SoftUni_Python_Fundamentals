money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integer = []

for money in money_as_string:
    money_as_integer.append(int(money))

beggars_sum = []
start_index = 0

for current_beggars in range(number_of_beggars):
    current_beggars_sum = 0
    for index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggars_sum += money_as_integer[index]
    beggars_sum.append(current_beggars_sum)
    start_index += 1

print(beggars_sum)