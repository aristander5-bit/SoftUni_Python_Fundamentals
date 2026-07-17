import re

matches = []
line = input()

while line:
    pattern = "\d+"
    match = re.findall(pattern, line)
    # if match:
    matches += match
    line = input()

print(" ".join(matches))