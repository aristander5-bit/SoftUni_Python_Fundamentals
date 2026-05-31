money_as_string = input().split(", ")
number_of_beggars = int(input())

money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))

beggars_sum = []

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0

    for index in range(current_beggar, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[index]

    beggars_sum.append(current_beggar_sum)

print(beggars_sum)
