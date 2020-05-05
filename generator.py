import copy
import random as rnd
import solver


def generate_sudoku(difficulty):
    board = solver.SudokuBoard([[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 8]])

    def trans():
        nonlocal board
        t = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board)):
                board[i][j] = t[j][i]

    def swap_row():
        nonlocal board
        line1 = rnd.randint(0, 8)
        line2 = (line1 // 3) * 3 + (line1 % 3 + rnd.randint(1, 2)) % 3
        board[line1], board[line2] = board[line2], board[line1]

    def swap_column():
        nonlocal board
        column1 = rnd.randint(0, 8)
        column2 = (column1 // 3) * 3 + (column1 % 3 + rnd.randint(1, 2)) % 3
        for i in range(9):
            board[i][column1], board[i][column2] = board[i][column2], board[i][column1]

    def swap_rows():
        nonlocal board
        row1 = rnd.randint(0, 2)
        row2 = (row1 + rnd.randint(1, 2)) % 3
        for i in range(9):
            board[row1 * 3][i], board[row2 * 3][i] = board[row2 * 3][i], board[row1 * 3][i]
            board[row1 * 3 + 1][i], board[row2 * 3 + 1][i] = board[row2 * 3 + 1][i], board[row1 * 3 + 1][i]
            board[row1 * 3 + 2][i], board[row2 * 3 + 2][i] = board[row2 * 3 + 2][i], board[row1 * 3 + 2][i]

    def swap_columns():
        nonlocal board
        column1 = rnd.randint(0, 2)
        column2 = (column1 + rnd.randint(1, 2)) % 3
        for i in range(9):
            board[i][column1 * 3], board[i][column2 * 3] = board[i][column2 * 3], board[i][column1 * 3]
            board[i][column1 * 3 + 1], board[i][column2 * 3 + 1] = board[i][column2 * 3 + 1], board[i][column1 * 3 + 1]
            board[i][column1 * 3 + 2], board[i][column2 * 3 + 2] = board[i][column2 * 3 + 2], board[i][column1 * 3 + 2]

    commands = {0: 'trans()', 1: 'swap_row()', 2: 'swap_column()', 3: 'swap_rows()', 4: 'swap_columns()'}
    for i in range(20):
        eval(commands[rnd.randint(0, 4)])
    for i in range(difficulty*10):
        x, y = rnd.randint(0, 8), rnd.randint(0, 8)
        if board[x][y] != '':
            t = board[x][y]
            board[x][y] = ''
            if board.num_of_solutions() != 1:
                board[x][y] = t
    return board
