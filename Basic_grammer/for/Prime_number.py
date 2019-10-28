
x = int(input())
a = 1
b = 0

for i in range(2, int(x / 2) + 1):
    if(x % i == 0):
        b = 1
        break

if(b == 0):
    print("소수")

else: print("소수 아님")