factor = int(input())
count = int(input())
numbers = []

for multiplier in range(1, count + 1):
    current_number = factor * multiplier
    numbers.append(current_number)

print(numbers)