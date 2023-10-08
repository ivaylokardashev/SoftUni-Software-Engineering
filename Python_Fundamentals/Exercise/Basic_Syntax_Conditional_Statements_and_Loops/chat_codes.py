number_of_massages = int(input())
text = ""
for current_massage in range(number_of_massages):
    number = int(input())
    if number == 88:
        text = "Hello"
    elif number == 86:
        text = "How are you?"
    elif number < 88:
        text = "GREAT!"
    else:
        text = "Bye."

    print(f"{text}")