
#add 더하기 sub 빼기 mul 곱하기 div 나누기

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a / b
    return c

while(True):

    x = int(input())

    if(x == 1):
        temp = int(input())
        temp_2 = int(input())
        print(add(temp, temp_2))

    elif(x == 2):
        temp = int(input())
        temp_2 = int(input())
        sub(temp, temp_2)

    elif(x == 3):
        temp = int(input())
        temp_2 = int(input())
        mul(temp, temp_2)

    elif(x == 4):
        temp = int(input())
        temp_2 = int(input())
        div(temp, temp_2)