list_str = input().split()
numbers = []

for i in list_str:
    real_number = int(i)
    numbers.append(int(i))
    
n = int(input())

for i in range(n):
    smallest_number = min(numbers)
    numbers.remove(smallest_number)

numbers_as_string = [str(num) for num in numbers]

print(", ".join(numbers_as_string))
