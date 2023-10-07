n_loops = int(input())
needed_word = input()
my_list = []
my_list_with_only_needed_sentence = []
for current_loop in range(n_loops):
    sentence = input()
    my_list.append(sentence)
    if needed_word in sentence:
        my_list_with_only_needed_sentence.append(sentence)
print(my_list)
print(my_list_with_only_needed_sentence)
