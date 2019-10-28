
def temp(x, y):
        for i in range(0, len(x)):

            if (len(x) != len(y)):
                flag = 0
                break

            elif(x[i] == y[i]):
                flag = 1

            elif(x[i] != y[i]):
                flag = 0
                break

        if(flag == 1):
                print("same")

        elif(flag == 0):
                print("different")

        return x, y


flag = 0

while(True):

    a = input()
    b = input()

    print(temp(a, b))