
class delete_word:

    def __init__(self):

        self.i_word = input_word
        self.o_word = output_word
        self.c = count
        self.c_word = count_word

    def delete (self, i_word, o_word, c, c_word):

        for i in range(0, len(i_word) - 1):

            if(i_word[i] < i_word[i + 1]):
                o_word.append(i_word[i])

            elif(i_word[i] > i_word[i + 1]):
                c = c + 1
                c_word.append(i_word[i])


input_word = str(input())
output_word = []
count = 0
count_word = []

delete_2 = delete_word()

delete_2.delete(input_word, output_word, count, count_word)

print("제거된 알파벳", count_word)
print("출력된 알파벳", output_word)
print(count)