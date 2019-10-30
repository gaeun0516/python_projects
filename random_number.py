
import random

while(True):
    input_word = int(input())
    num_1 = random.randrange(1, 30)
    num_2 = random.randrange(1, 10)

    if(input_word == 1):
        print(num_1, "+", num_2, "=", num_1 + num_2)

    elif(input_word == 2):
        print(num_1, "-", num_2, "=", num_1 - num_2)

    elif(input_word == 3):
        print(num_1, "/", num_2, "=", num_1 / num_2)

    elif(input_word == 4):
        print(num_1, "*", num_2, "=", num_1 * num_2)