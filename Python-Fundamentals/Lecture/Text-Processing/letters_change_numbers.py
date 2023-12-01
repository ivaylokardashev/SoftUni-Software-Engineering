def test(text):
    total = 0
    num = ""
    letter_before_num = ""

    for word in text:
        if word.isalpha():
            if num is not "":
                letter_after_num = word
                if letter_before_num.isupper():
                    total += int(num) / int(ord(letter_before_num.lower()) - 96)
                else:
                    total += int(num) * int(ord(letter_before_num) - 96)
                if letter_after_num.isupper():
                    total -= int(ord(letter_after_num.lower()) - 96)
                else:
                    total += int(ord(letter_after_num) - 96)
                num = ""
            letter_before_num = word
        elif word.isdigit():
            num += word

    return total


word = input().split()
the_real_word = " ".join(word)
print(f"{test(the_real_word):.2f}")
