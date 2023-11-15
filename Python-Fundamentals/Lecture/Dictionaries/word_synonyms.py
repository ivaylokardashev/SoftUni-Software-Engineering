n = int(input())
dictionary = {}
for current_word_and_synonym in range(n):
    word = input()
    synonym = input()

    if word not in dictionary.keys():
        dictionary[f"{word}"] = []
    dictionary[f"{word}"].append(synonym)

for (key, value) in dictionary.items():
    all_synonyms = ', '.join(value)
    print(f"{key} - {all_synonyms}")
