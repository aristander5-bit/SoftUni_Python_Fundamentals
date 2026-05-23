number_lines = int(input())

bracket_balance = 0
is_balanced = True

for i in range(number_lines):
    line = input()

    if line == "(":
        bracket_balance += 1
    elif line == ")":
        bracket_balance -= 1

    if bracket_balance < 0 or bracket_balance > 1:
        is_balanced = False
        break

if bracket_balance != 0:
    is_balanced = False


if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")