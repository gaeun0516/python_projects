def select_first():

    select = input()
    o = 0
    x = 1

    if(select == o):
        return o

    elif(select == x):
        return x

def select_shape():

    select = input()
    o = "o"
    x = "x"

    if(select == o):
        return o

    elif(select == x):
        return x

def made_board():

    board_list = []

    for i in range(9):
        board_list.append("*")

    return board_list

def select_room(board, shape):

    while(True):

        room = int(input())

        if(board[room] == "*"):
            board[room] = shape
            break

        elif(board[room] != "*"):
            print ("again select")

    return board

def show_board(board):

    for i in range(3):
        print (board[i * 3], board[i * 3 + 1], board[i * 3 + 2])

board_list = []
user_shape = "o"



for i in range(9):
    board_list.append("*")
select_room(board_list, user_shape)