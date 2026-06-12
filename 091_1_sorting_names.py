names = input().split(', ')

names.sort()

names.sort(key=lambda name: len(name), reverse=True)
print(names)