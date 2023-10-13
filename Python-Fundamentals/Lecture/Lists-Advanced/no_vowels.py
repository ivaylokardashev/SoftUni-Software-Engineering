text_with_vowels = input()

vowels = ['a', 'o', 'u', 'e', 'i']
text_without_vowels = [x for x in text_with_vowels if x.lower() not in vowels]

for char in text_without_vowels:
    print(char, end="")
