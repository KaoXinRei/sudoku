import tkinter as tk
import tkinter.ttk as ttk
from solver import SudokuBoard
from generator import generate_sudoku


class Window(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.key_binds()
        self.buttons_bind()

    def create_variables(self):
        self.vars = [tk.StringVar() for _ in range(81)]
        for i in range(81):
            self.vars[i].set('')
        self.board = SudokuBoard([['' for _ in range(9)] for _ in range(9)])

    def create_widgets(self):
        self.cells = [
            ttk.Entry(self, textvariable=self.vars[i], state='readonly', width=3, font='Calibri 15', justify='center')
            for i in
            range(81)]
        self.generate_button = ttk.Button(self, text='Generate sudoku')
        self.solve_button = ttk.Button(self, text='Solve sudoku')
        self.clear_button = ttk.Button(self, text='Clear')
        self.vsep1 = tk.Frame(self, width=2, bg='black')
        self.vsep2 = tk.Frame(self, width=2, bg='black')
        self.hsep1 = tk.Frame(self, height=2, bg='black')
        self.hsep2 = tk.Frame(self, height=2, bg='black')
        self.dif_label = ttk.Label(self, text='Difficulty:', justify='center')
        self.scale = tk.Scale(self, from_=1, to=10, orient='horizontal')
        self.scale.set(5)

    def create_layout(self):
        for i in range(9):
            for j in range(9):
                self.cells[i * 9 + j].grid(row=i + i // 3, column=j + j // 3, padx=1, pady=1)
        self.vsep1.grid(row=0, column=3, rowspan=11, sticky=(tk.N, tk.S))
        self.vsep2.grid(row=0, column=7, rowspan=11, sticky=(tk.N, tk.S))
        self.hsep1.grid(row=3, column=0, columnspan=11, sticky=(tk.E, tk.W))
        self.hsep2.grid(row=7, column=0, columnspan=11, sticky=(tk.E, tk.W))
        self.generate_button.grid(row=0, column=11, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.solve_button.grid(row=1, column=11, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.clear_button.grid(row=2, column=11, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.dif_label.grid(row=4, column=11, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.scale.grid(row=5, column=11, rowspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.rowconfigure(4, weight=1)
        self.columnconfigure(11, weight=1)

    def click_1(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 1):
            self.vars[a].set(1)
            self.board[a // 9][a % 9] = 1

    def click_2(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 2):
            self.vars[a].set(2)
            self.board[a // 9][a % 9] = 2

    def click_3(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 3):
            self.vars[a].set(3)
            self.board[a // 9][a % 9] = 3

    def click_4(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 4):
            self.vars[a].set(4)
            self.board[a // 9][a % 9] = 4

    def click_5(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 5):
            self.vars[a].set(5)
            self.board[a // 9][a % 9] = 5

    def click_6(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 6):
            self.vars[a].set(6)
            self.board[a // 9][a % 9] = 6

    def click_7(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 7):
            self.vars[a].set(7)
            self.board[a // 9][a % 9] = 7

    def click_8(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 8):
            self.vars[a].set(8)
            self.board[a // 9][a % 9] = 8

    def click_9(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        if self.board.valid(a // 9, a % 9, 9):
            self.vars[a].set(9)
            self.board[a // 9][a % 9] = 9

    def click_0(self, event):
        a = str(self.master.focus_get())[15:]
        if a == '':
            a = 1
        a = int(a) - 1
        self.vars[a].set('')

    def click_solve(self, event):
        self.board.solved = False
        for i in range(9):
            for j in range(9):
                try:
                    self.board[i][j] = int(self.vars[i * 9 + j].get())
                except:
                    self.board[i][j] = ''
        self.board.solve()
        for i in range(9):
            for j in range(9):
                self.vars[i * 9 + j].set(str(self.board[i][j]))

    def click_generate(self, event):
        self.board = generate_sudoku(self.scale.get())
        for i in range(9):
            for j in range(9):
                self.vars[i * 9 + j].set(str(self.board[i][j]))

    def click_clear(self, event):
        for i in range(81):
            self.vars[i].set('')

    def buttons_bind(self):
        self.generate_button.bind('<Button-1>', self.click_generate)
        self.solve_button.bind('<Button-1>', self.click_solve)
        self.clear_button.bind('<Button-1>', self.click_clear)

    def key_binds(self):
        self.master.bind_all('1', self.click_1)
        self.master.bind_all('2', self.click_2)
        self.master.bind_all('3', self.click_3)
        self.master.bind_all('4', self.click_4)
        self.master.bind_all('5', self.click_5)
        self.master.bind_all('6', self.click_6)
        self.master.bind_all('7', self.click_7)
        self.master.bind_all('8', self.click_8)
        self.master.bind_all('9', self.click_9)
        self.master.bind_all('0', self.click_0)
        self.master.bind_all('<Return>', self.click_solve)
        self.master.bind_all('<BackSpace>', self.click_0)
        self.master.bind_all('<Delete>', self.click_clear)
