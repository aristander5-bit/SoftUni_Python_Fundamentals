def check_multiplication_sign(num_1: int, num_2: int, num_3: int):
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        print("zero")
        return
    negative_count = 0

    if num_1 < 0:
        negative_count += 1
    if num_2 < 0:
        negative_count += 1
    if num_3 < 0:
        negative_count += 1

    if negative_count == 1 or negative_count == 3:
        print("negative")
    else:
        print("positive")

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

check_multiplication_sign(number_1, number_2, number_3)