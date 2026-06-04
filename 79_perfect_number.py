def check_perfect_number(number:int) -> str:
    divisors = 0

    for current_num in range(1, number):
        if number % current_num == 0:
            divisors += current_num

    if divisors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

input_number = int(input())

result = check_perfect_number(input_number)
print(result)