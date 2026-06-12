def solve_data_types(data_types: str, value : str):
    if data_types == "int":
        result = int(value)
        result *= 2
        print(result)
    elif data_types == "real":
        result = float(value)
        result *= 1.5
        print(f"{result:.2f}")
    elif data_types == "string":
        result = value
        print(f"${result}$")

command = input()
data = input()
solution = solve_data_types(command, data)