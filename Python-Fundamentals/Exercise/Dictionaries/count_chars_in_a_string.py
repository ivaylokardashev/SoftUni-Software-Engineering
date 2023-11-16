words = input()
char_counter = {}

for word in words:
    if word != ' ':
        if word not in char_counter.keys():
            char_counter[f"{word}"] = 0

        char_counter[f"{word}"] += 1

for (key, value) in char_counter.items():
    print(f"{key} -> {value}")
