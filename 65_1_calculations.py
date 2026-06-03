def calculate_result(operator, num_1, num_2):
    return {
        "multiply": num_1 * num_2,
        "divide": int(num_1 / num_2),
        "add": num_1 + num_2,
        "subtract": num_1 - num_2,
    }.get(operator, "Invalid operator")

operator = input("Enter the operator (multiply, divide, add, subtract): ")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
result = calculate_result(operator,num_1,num_2)
print(f"{result}")