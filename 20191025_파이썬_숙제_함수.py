
def delete (input_word, output_word, count, count_word):

    for i in range(0, len(input_word) - 1):

        if(input_word[i] < input_word[i + 1]):
            output_word.append(input_word[i])

        elif(input_word[i] > input_word[i + 1]):
            count = count + 1
            count_word.append(input_word[i])

    return input_word, output_word, count, count_word

input_word = str(input())
output_word = []
count = 0
count_word = []

delete(input_word, output_word, count, count_word)

print("제거된 알파벳", count_word)
print("출력된 알파벳", output_word)
print(count)