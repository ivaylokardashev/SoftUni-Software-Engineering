while True:
    word = input()
    if word == "End":
        break
    elif word != "SoftUni":
        double_word = ""
        for char in word:
            double_word += char * 2
        print(double_word)

