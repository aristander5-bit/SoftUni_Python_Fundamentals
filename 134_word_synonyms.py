n = int(input())
synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonyms in synonyms.items():
    synonym_str = ', '.join(synonyms)
    print(f"{word} - {synonym_str}")
