
x = int(input())
y = 1
a = 1
b = 100


for i in range(100):
    c = int((a + b) / 2)

    if(x == c):
        print(y)
        break
    elif(x > c):
        a = c
    elif(x < c):
        b = c
    y = y + 1