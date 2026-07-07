contests = {}
users = {}

while True:
    line = input()
    if line == "end of contests":
        break

    data = line.split(":")
    contest = data[0]
    password = data[1]

    contests[contest] = password

while True:
    line = input()
    if line == "end of submissions":
        break

    data = line.split("=>")
    contest = data[0]
    password = data[1]
    username = data[2]
    points = int(data[3])

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username]:
            users[username][contest] = points
        else:
            if points > users[username][contest]:
                users[username][contest] = points

best_user = ""
max_points = 0

for username, contest_data in users.items():
    total_points = sum(contest_data.values())
    if total_points > max_points:
        max_points = total_points
        best_user = username

print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")

for username in sorted(users.keys()):
    print(username)

    sorted_contest = sorted(users[username].items(), key=lambda x: x[1], reverse=True)
    for contest, points in sorted_contest:
        print(f"# {contest} -> {points}")


