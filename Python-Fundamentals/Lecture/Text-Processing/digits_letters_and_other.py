text = input()
digit = ""
letters = ""
other_chars = ""

for word in text:
    if word.isnumeric():
        digit += word
    elif word.isalpha():
        letters += word
    else:
        other_chars += word

print(digit)
print(letters)
print(other_chars)
