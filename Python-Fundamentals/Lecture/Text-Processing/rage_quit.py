text = input()
unique_symbols = ""
repetitions = ""
current_symbols = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index].upper()
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        unique_symbols += current_symbols * int(repetitions)
        current_symbols = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
