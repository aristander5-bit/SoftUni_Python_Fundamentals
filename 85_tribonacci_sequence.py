def tribonacci(num : int):
    sequence = [1, 1 , 2]

    if num <= 3:
        result = sequence[:num]
    else:
        for i in range(num - 3):
            next_num = sequence[-1] + sequence[-2] + sequence[-3]
            sequence.append(next_num)
        result = sequence

    print(*result)

num = int(input())
tribonacci(num)