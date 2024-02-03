real_word = input()
unique_word = sorted(list(set(real_word)))

for current_word in unique_word:
    print(f"{current_word}: {real_word.count(current_word)} time/s")

