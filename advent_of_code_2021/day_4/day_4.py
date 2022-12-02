# # Question: https://adventofcode.com/2021/day/4
# Part 1 ------------------------------------------------

class Board:

    def __init__(self, board):
        self.board = board
        self.unmarkedBoard = [[True for i in range(5)] for j in range(5)]

    def markBoard(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.unmarkedBoard[i][j] = False
                    break

    def checkBoard(self, number):
        for row in self.unmarkedBoard:
            if row == [False for i in range(5)]:
                return self.getTotal() * number
        for i in range(5):
            if [self.unmarkedBoard[j][i] for j in range(5)] == [False for i in range(5)]:
                return self.getTotal() * number
        if [self.unmarkedBoard[i][i] for i in range(5)] == [False for i in range(5)]:
            return self.getTotal() * number
        if [self.unmarkedBoard[i][4 - i] for i in range(5)] == [False for i in range(5)]:
            return self.getTotal() * number
        return -1

    def getTotal(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if self.unmarkedBoard[i][j]:
                    total += self.board[i][j]
        return total


def part_1(list_of_boards, numbers_drawn):
    done = False
    currentIndex = 0
    while not done and currentIndex < len(numbers_drawn):
        for i in range(len(list_of_boards)):
            list_of_boards[i].markBoard(numbers_drawn[currentIndex])
            check = list_of_boards[i].checkBoard(numbers_drawn[currentIndex])
            if check > 0:
                done = True
                break
        currentIndex += 1
    return check


def part_2(list_of_boards,numbers_drawn):
    currentIndex = 0
    CHECKS = 5
    while len(list_of_boards) > 1:
        for c in range(CHECKS):
            for i in range(len(list_of_boards)-1, -1, -1):
                list_of_boards[i].markBoard(numbers_drawn[currentIndex])
                check = list_of_boards[i].checkBoard(numbers_drawn[currentIndex])
                if check > 0 and len(list_of_boards) > 1:
                    doneBoard=list_of_boards.pop(i)
                    i -= 1
                    break
        currentIndex += 1
    print(list_of_boards[0].board)
    print(numbers_drawn[currentIndex-1])
    # done = False
    # while not done and currentIndex < len(numbers_drawn):
    #     list_of_boards[0].markBoard(numbers_drawn[currentIndex])
    #     check = list_of_boards[0].checkBoard(numbers_drawn[currentIndex])
    #     if check > 0:
    #         done = True
    #         print(check)
    #         break
    #     currentIndex += 1
    # print(part_1(list_of_boards[0], numbers_drawn))
    # print(list_of_boards[0].board)
    # print(list_of_boards[0].getTotal())
    # print(list_of_boards[0].getTotal()-numbers_drawn[currentIndex])
    # print(numbers_drawn[currentIndex])
    print((list_of_boards[0].getTotal()-numbers_drawn[currentIndex-1]))
    return (list_of_boards[0].getTotal()-numbers_drawn[currentIndex-1])*numbers_drawn[currentIndex - 1]
    # return 0


def get_board_and_numbers_drawn():
    input = open('input.txt', 'r').read().split('\n')
    numbers_drawn = [int(x) for x in input[0].split(',')]
    input.pop(0)
    list_of_boards = []
    board = []
    for index, row in enumerate(input):
        if row == '':
            list_of_boards.append(Board(board))
            board = []
        else:
            board.append([int(x) for x in row.split(' ') if x != ''])
    list_of_boards.pop(0)
    list_of_boards.append(Board(board))
    return list_of_boards, numbers_drawn

bingo_boards, bingo_numbers = get_board_and_numbers_drawn()

print(part_2(bingo_boards, bingo_numbers))
