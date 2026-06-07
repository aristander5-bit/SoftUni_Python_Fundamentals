from math import floor

def find_closest_point(x_1: float, y_1: float, x_2: float, y_2: float):
    dist_1 = x_1 ** 2 + y_1 ** 2
    dist_2 = x_2 ** 2 + y_2 ** 2
    if dist_1 <= dist_2:
        final_x = floor(x_1)
        final_y = floor(y_1)
    else:
        final_x = floor(x_2)
        final_y = floor(y_2)

    print(f"({final_x}, {final_y})")

num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())

find_closest_point(num_1, num_2, num_3, num_4)

