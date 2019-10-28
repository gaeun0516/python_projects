
#최대공약수 구하기

a = int(input())
b = int(input())
temp = b
c = 0


if(a < b):
    temp = a

for i in range(1, temp + 1):
    if(a % i == 0 and b % i == 0):
        c = i

print(c)