from tkinter import *
from tkinter import messagebox

root = Tk()

player_letter = "X"
DEFAULT = " "
buttons = []


def winner(letter: str = player_letter):
    board = []

    # extract text from buttons
    for button in buttons:
        board.append(button["text"])

    # check for wining
    if (board[0] is letter) and (board[1] is letter) and (board[2] is letter) \
        or (board[3] is letter) and (board[4] is letter) and (board[5] is letter) \
        or (board[6] is letter) and (board[7] is letter) and (board[8] is letter) \
        or (board[0] is letter) and (board[3] is letter) and (board[6] is letter) \
        or (board[1] is letter) and (board[4] is letter) and (board[7] is letter) \
        or (board[2] is letter) and (board[5] is letter) and (board[8] is letter) \
        or (board[0] is letter) and (board[4] is letter) and (board[8] is letter) \
        or (board[2] is letter) and (board[4] is letter) and (board[6] is letter):
        return True
    else:
        return False


def play(position):
    # button configuration
    buttons[position].config(text=player_letter, state="disabled", relief=FLAT)

    # check for winning
    if winner(player_letter):
        messagebox.showinfo("congratulations", "you are the winner")
        if messagebox.askyesno("what to do next?", "do you want to play again? if not, the game will close."):
            for button in buttons:
                button.config(text=DEFAULT, state=NORMAL, relief=RAISED)
        else:
            root.destroy()


# for number in range(9):
#     i = number
#     buttons.append(Button(root, text=number, command=lambda: play(i)))
#     row, column = number // 3, number % 3
#     buttons[number].grid(row=row, column=column)
#     # button[number].bind('<Button>', lambda: play(number))

# first row
buttons.append(Button(root, text=DEFAULT, command=lambda: play(0)))
buttons[0].grid(row=0, column=0)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(1)))
buttons[1].grid(row=0, column=1)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(2)))
buttons[2].grid(row=0, column=2)

# second row
buttons.append(Button(root, text=DEFAULT, command=lambda: play(3)))
buttons[3].grid(row=1, column=0)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(4)))
buttons[4].grid(row=1, column=1)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(5)))
buttons[5].grid(row=1, column=2)

# third row
buttons.append(Button(root, text=DEFAULT, command=lambda: play(6)))
buttons[6].grid(row=2, column=0)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(7)))
buttons[7].grid(row=2, column=1)

buttons.append(Button(root, text=DEFAULT, command=lambda: play(8)))
buttons[8].grid(row=2, column=2)

root.mainloop()


