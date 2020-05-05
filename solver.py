import copy


class SudokuBoard(list):
    def __init__(self, val):
        self.solved = False
        super().__init__(val)

    def valid(self, x, y, n):
        if n in self[x]:
            return False
        if n in [self[i][y] for i in range(9)]:
            return False
        x0 = x // 3 * 3
        y0 = y // 3 * 3
        for i in range(3):
            for j in range(3):
                if self[x0 + i][y0 + j] == n:
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self[i][j] == '':
                    for n in range(1, 10):
                        if self.valid(i, j, n):
                            self[i][j] = n
                            self.solve()
                            if self.solved:
                                return
                            self[i][j] = ''
                    return
        self.solved = True

    def num_of_solutions(self):
        num = 0
        temp = SudokuBoard(copy.deepcopy(self))

        def solve(board):
            nonlocal num
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '':
                        for n in range(9):
                            if board.valid(i, j, n + 1):
                                board[i][j] = n + 1
                                solve(board)
                                board[i][j] = ''
                        return
            num += 1

        solve(temp)
        return num


