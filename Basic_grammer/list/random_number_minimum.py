
import random

x = []

for i in range(10):
    y = random.randrange(1, 100)
    x.append(y)

print(x)


for i in range(len(x)):
    print(x[i])


a = x[0]

for i in range(1, len(x)):

    if(a > x[i]):
        a = x[i]

print("최솟값 :", a)