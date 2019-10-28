
import random

x = []

for i in range(10):
    y = random.randrange(1, 100)
    x.append(y)

print(x)


for i in range(len(x)):
    print(x[i])


a = 0
b = x[0]

for i in range(1, len(x)):

    if(b > x[i]):
        b = b
    else: b = x[i]

print("최댓값 :", b)