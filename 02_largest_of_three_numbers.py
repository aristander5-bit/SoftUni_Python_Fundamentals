
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3


print(largest)