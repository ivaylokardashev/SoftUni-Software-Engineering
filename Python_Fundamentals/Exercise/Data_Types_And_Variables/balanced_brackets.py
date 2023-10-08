n = int(input())
OPENING_BRACKETS = '('
CLOSING_BRACKETS = ')'
balanced_brackets_flag = False
count_of_opening_brackets = 0

for _ in range(n):
    char = input()

    if OPENING_BRACKETS == char:
        balanced_brackets_flag = True
        count_of_opening_brackets += 1
        if count_of_opening_brackets == 2:
            print("UNBALANCED")
            break
    elif CLOSING_BRACKETS == char:
        if not balanced_brackets_flag:
            print("UNBALANCED")
            break
        else:
            balanced_brackets_flag = False
            count_of_opening_brackets = 0
else:
    print("BALANCED")