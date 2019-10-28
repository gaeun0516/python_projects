
for i in range(10):
    print ("*" * i)

for i in range(10):
    print ("*" * (10 - i))

for i in range(1, 100):

    ten = int(i/10)
    one = i%10
    ten_true = False
    one_true = False

    if (ten == 3 or ten == 6 or ten == 9):
        ten_true = True
    if (one == 3 or one == 6 or one == 9):
        one_true = True

    if (ten_true and one_true):
        print ("**")
    elif (ten_true or one_true):
        print ("*")
    else: print (i)

