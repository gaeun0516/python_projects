
def find_word(input_word, list_word, same_list):

    for i in range(0, len(input_word)):
        flag = 0
        for o in range(0, len(list_word)):
            if(input_word[i] == list_word[o]):
                flag = 1
                break

        if(flag == 1):
            same_list.append(input_word[i])

    return input_word, list_word, same_list


i_word = input()
l_word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
same_word = []

find_word(i_word, l_word, same_word)

print(same_word)
