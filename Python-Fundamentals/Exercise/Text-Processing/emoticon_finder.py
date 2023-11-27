sentence = input()

for word in range(0, len(sentence)):
    if sentence[word] == ":":
        print(f"{sentence[word]}{sentence[word + 1]}")

