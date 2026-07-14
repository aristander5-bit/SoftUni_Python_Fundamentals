import re

pattern = r'(^|(?<=\s))-?(?:0|[1-9]\d*)(?:\.\d+)?(?=$|\s)'

text = input()

matches = re.finditer(pattern, text)

for match in matches:

    print(match.group(), end=" ")