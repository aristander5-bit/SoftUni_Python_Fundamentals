def check_palindromes(numbers_strings):
    for number in numbers_strings:
        reversed_str = number[::-1]

        if number == reversed_str:
            print(True)
        else:
            print(False)


input_data = input().split(", ")

check_palindromes(input_data)
