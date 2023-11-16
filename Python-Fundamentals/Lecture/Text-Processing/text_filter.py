baned_words = input().split(", ")
text = input()

for baned_word in baned_words:
    while baned_word in text:
        text = text.replace(baned_word, '*'*len(baned_word))

print(text)
