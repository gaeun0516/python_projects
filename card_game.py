
class cardChoice:

    def choice(self, board, num_list):
        while True:
            #board는 공백 리스트 num_list는 숫자 리스트
            card_1 = int(input())
            card_2 = int(input())

            #같을 경우
            if num_list[card_1] == num_list[card_2]:
                board[card_1], board[card_2] = num_list[card_1], num_list[card_2]
            #다를 경우
            elif num_list[card_1] != num_list[card_2]:
                board[card_1], board[card_2] = '#', '#'
            #이미 선택했던 칸을 고른 경
            elif board[card_1] != '#' or board[card_2] != '#':
                print 'again choice'

        return board
