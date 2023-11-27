sentence = input()
encrypted_sentence = ""

for word in sentence:
    encrypted_sentence += chr(ord(word) + 3)

print(encrypted_sentence)
