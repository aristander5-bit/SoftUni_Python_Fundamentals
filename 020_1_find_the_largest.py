number = int(input())

for current_digit in range(9,-1, -1):
    temp_number= number

    while temp_number > 0:
        last_digit = temp_number % 10

        if last_digit == current_digit:
            print(last_digit, end="")

        temp_number = temp_number // 10