
input_word = str(input())
count = 0
del_word = []
output_word = []

for i in range(0, len(input_word) - 1):

    if(i == len(input_word) - 2):
        if(input_word[len(input_word) - 2] > input_word[len(input_word) - 1]):
            del_word.append(input_word[len(input_word) - 1])
            output_word.append(input_word[i])


    elif(input_word[i] > input_word[i + 1]):
        count = count + 1
        del_word.append(input_word[i])

    elif(input_word[i] < input_word[i + 1]):
        output_word.append(input_word[i])


print("제거된 알파벳", del_word)
print("출력된 알파벳", output_word)
print(count)
