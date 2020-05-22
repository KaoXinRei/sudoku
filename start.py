import tkinter as tk
import gui


def main():
    root = tk.Tk()
    gui.Window(root)
    root.title('Sudoku')
    root.minsize(width=400, height=250)
    root.mainloop()


main()
