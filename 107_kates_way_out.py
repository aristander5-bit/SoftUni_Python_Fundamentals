number_rows = int(input())
maze = []
kate_row = 0
kate_col = 0

for row in range(number_rows):
    current_row = list(input())
    maze.append(current_row)

    if "k" in current_row:
        kate_row = row
        kate_col = current_row.index("k")

position_to_explore = [(kate_row, kate_col, 1)]
max_moves = 0
visited = set()
visited.add((kate_row, kate_col))

while position_to_explore:
    current_row, current_col, current_moves = position_to_explore.pop(0)

    if current_row == 0 or current_row == number_rows - 1 \
            or current_col == 0 or current_col == len(maze[0]) - 1:
        if current_moves > max_moves:
            max_moves = current_moves
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move_r, move_c in directions:
        next_row, next_col = current_row + move_r, current_col + move_c

        if 0 <= next_row < number_rows and 0 <= next_col < len(maze[0]):
            if maze[next_row][next_col] == " " and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                position_to_explore.append((next_row, next_col, current_moves + 1))

if max_moves > 0:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")