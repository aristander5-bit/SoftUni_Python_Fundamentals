def calculate_rectangle_area(width, height):
    area = width * height
    return area

current_width = int(input())
current_height = int(input())

result = calculate_rectangle_area(current_width, current_height)
print(result)