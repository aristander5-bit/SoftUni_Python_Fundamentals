from math import floor

def find_longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    line_1_length = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
    line_2_length = (x_3 - x_4) ** 2 + (y_3 - y_4) ** 2

    if line_1_length >= line_2_length:
        if (x_1**2 + y_1**2) <= (x_2**2 + y_2**2):
            start_x, start_y = floor(x_1), floor(y_1)
            end_x, end_y = floor(x_2), floor(y_2)
        else:
            start_x, start_y = floor(x_2), floor(y_2)
            end_x, end_y = floor(x_1), floor(y_1)
    else:
        if (x_3**2 + y_3**2) <= (x_4**2 + y_4**2):
            start_x, start_y = floor(x_3), floor(y_3)
            end_x, end_y = floor(x_4), floor(y_4)
        else:
            start_x, start_y = floor(x_4), floor(y_4)
            end_x, end_y = floor(x_3), floor(y_3)


    print(f"({start_x}, {start_y})({end_x}, {end_y})")

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
num_6 = float(input())
num_7 = float(input())
num_8 = float(input())

find_longer_line(num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8)