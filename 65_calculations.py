def calculate_result(operator, num_1, num_2):


    if operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    elif operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        if num_2 != 0:
            result = num_1 // num_2

    return result

input_operator = input()
first_num = int(input())
second_num = int(input())


print(calculate_result(input_operator, first_num, second_num))