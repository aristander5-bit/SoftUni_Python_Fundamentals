numbers = [int(x) for x in input().split()]

middle = len(numbers) // 2
left_track = numbers[:middle]
right_track = numbers[middle + 1:][::-1]

left_time = 0
right_time = 0

for time in left_track:
    if time == 0:
        left_time *= 0.80
    else:
        left_time += time

for time in right_track:
    if time == 0:
        right_time *= 0.80
    else:
        right_time += time
if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")