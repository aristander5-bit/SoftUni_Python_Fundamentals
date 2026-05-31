numbers = [int(x) for x in input().split()]
n = int(input())

for i in range(n):
    smallest_number = min(numbers)
    numbers.remove(smallest_number)

numbers_as_string = [str(num) for num in numbers]

print(", ".join(numbers_as_string))