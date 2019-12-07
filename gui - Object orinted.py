from tkinter import *
from tkinter import messagebox


class XO:
    """
    X/O game between 2 player
    """
    root = Tk()
    root.title("XO game")
    DEFAULT = " "
    letter = "X"
    buttons = []

    def __init__(self):
        self.load_widgets()
        self.root.mainloop()

    def load_widgets(self):
        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(0)))
        self.buttons[0].grid(row=0, column=0)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(1)))
        self.buttons[1].grid(row=0, column=1)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(2)))
        self.buttons[2].grid(row=0, column=2)

        # second row
        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(3)))
        self.buttons[3].grid(row=1, column=0)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(4)))
        self.buttons[4].grid(row=1, column=1)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(5)))
        self.buttons[5].grid(row=1, column=2)

        # third row
        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(6)))
        self.buttons[6].grid(row=2, column=0)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(7)))
        self.buttons[7].grid(row=2, column=1)

        self.buttons.append(Button(self.root, text=self.DEFAULT, command=lambda: self.play(8)))
        self.buttons[8].grid(row=2, column=2)

    def play(self, position: int):
        # button configuration
        self.buttons[position].config(text=self.letter, state="disabled", relief=FLAT)

        # check for winning
        if self.is_winner(self.get_board()):
            self.game_end()
        # check for draw
        elif self.is_full():
            self.game_end(draw=TRUE)

        # change letter
        self.change_letter()

    def get_board(self):
        board = []
        # extract text from buttons
        for button in self.buttons:
            board.append(button["text"])

        return board

    def is_winner(self, board):
        if (board[0] is self.letter) and (board[1] is self.letter) and (board[2] is self.letter) \
                or (board[3] is self.letter) and (board[4] is self.letter) and (board[5] is self.letter) \
                or (board[6] is self.letter) and (board[7] is self.letter) and (board[8] is self.letter) \
                or (board[0] is self.letter) and (board[3] is self.letter) and (board[6] is self.letter) \
                or (board[1] is self.letter) and (board[4] is self.letter) and (board[7] is self.letter) \
                or (board[2] is self.letter) and (board[5] is self.letter) and (board[8] is self.letter) \
                or (board[0] is self.letter) and (board[4] is self.letter) and (board[8] is self.letter) \
                or (board[2] is self.letter) and (board[4] is self.letter) and (board[6] is self.letter):
            return True
        else:
            return False

    def is_full(self):
        return self.DEFAULT not in self.get_board()

    def game_end(self, draw=FALSE):
        if draw is FALSE:
            title = "congratulations"
            message = self.letter + " is the winner"
        else:
            title = "unfortunately"
            message = "no one win!"

        messagebox.showinfo(title, message)
        if messagebox.askyesno("what to do next?", "do you want to play again? if not, the game will close."):
            for button in self.buttons:
                button.config(text=self.DEFAULT, state=NORMAL, relief=RAISED)
        else:
            self.root.destroy()

    def change_letter(self):
        self.letter = "X" if self.letter is "O" else "O"


# run the game
XO()
