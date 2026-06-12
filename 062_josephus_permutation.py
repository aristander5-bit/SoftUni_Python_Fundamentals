list_str = input().split()
people = []

for i in range(len(list_str)):
    people.append(int(list_str[i]))

k = int(input())
executed = []
index = 0

while len(people) > 0:
    index = (index + k - 1) % len(people)

    dead_person = people.pop(index)
    executed.append(dead_person)

executed_as_str = []
for j in executed:
    executed_as_str.append(str(j))

print("[" + ",".join(executed_as_str) + "]")


