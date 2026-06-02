import tkinter as tk
from tkinter import messagebox
import random

# Main Window

root = tk.Tk()
root.title("AI Tic Tac Toe")
root.geometry("420x520")
root.config(bg="#0f172a")

# Game Variables

board = [""] * 9
buttons = []

# Check Winner Function

def check_winner(player):

    winning_positions = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]
    ]

    for position in winning_positions:

        if (
            board[position[0]] ==
            board[position[1]] ==
            board[position[2]] == player
        ):

            return True

    return False

# Check Draw

def check_draw():

    return "" not in board

# Disable Buttons

def disable_buttons():

    for button in buttons:

        button.config(state="disabled")

# AI Move

def ai_move():

    # First Try To Win

    for i in range(9):

        if board[i] == "":

            board[i] = "O"

            if check_winner("O"):

                buttons[i].config(
                    text="O",
                    fg="#ef4444"
                )

                status_label.config(
                    text="AI Wins"
                )

                messagebox.showinfo(
                    "Game Over",
                    "AI Wins"
                )

                disable_buttons()

                return

            board[i] = ""

    # Block Player Winning Move

    for i in range(9):

        if board[i] == "":

            board[i] = "X"

            if check_winner("X"):

                board[i] = "O"

                buttons[i].config(
                    text="O",
                    fg="#ef4444"
                )

                # Check Draw After Blocking

                if check_draw():

                    status_label.config(
                        text="It's a Draw"
                    )

                    messagebox.showinfo(
                        "Game Over",
                        "It's a Draw"
                    )

                    disable_buttons()

                return

            board[i] = ""

    # Otherwise Random Move

    empty_positions = []

    for i in range(9):

        if board[i] == "":

            empty_positions.append(i)

    if empty_positions:

        position = random.choice(empty_positions)

        board[position] = "O"

        buttons[position].config(
            text="O",
            fg="#ef4444"
        )

    # Final Winner Check

    if check_winner("O"):

        status_label.config(
            text="AI Wins"
        )

        messagebox.showinfo(
            "Game Over",
            "AI Wins"
        )

        disable_buttons()

    elif check_draw():

        status_label.config(
            text="It's a Draw"
        )

        messagebox.showinfo(
            "Game Over",
            "It's a Draw"
        )

        disable_buttons()

# Player Move

def button_click(index):

    if board[index] == "":

        board[index] = "X"

        buttons[index].config(
            text="X",
            fg="#22c55e"
        )

        # Player Winner

        if check_winner("X"):

            status_label.config(
                text="You Win"
            )

            messagebox.showinfo(
                "Game Over",
                "You Win"
            )

            disable_buttons()

            return

        # Draw

        if check_draw():

            status_label.config(
                text="It's a Draw"
            )

            messagebox.showinfo(
                "Game Over",
                "It's a Draw"
            )

            disable_buttons()

            return

        # AI Turn

        ai_move()

# Restart Game

def restart_game():

    global board

    board = [""] * 9

    for button in buttons:

        button.config(
            text="",
            state="normal"
        )

    status_label.config(
        text="Your Turn (X)"
    )

# Title

title = tk.Label(

    root,

    text="AI Tic Tac Toe",

    font=("Arial", 24, "bold"),

    bg="#0f172a",

    fg="white"
)

title.pack(pady=20)

# Game Frame

game_frame = tk.Frame(
    root,
    bg="#0f172a"
)

game_frame.pack()

# Create Buttons

for i in range(9):

    button = tk.Button(

        game_frame,

        text="",

        font=("Arial", 30, "bold"),

        width=5,

        height=2,

        bg="#1e293b",

        fg="white",

        activebackground="#2563eb",

        relief="flat",

        cursor="hand2",

        command=lambda i=i:
        button_click(i)
    )

    button.grid(

        row=i//3,

        column=i%3,

        padx=5,

        pady=5
    )

    buttons.append(button)

# Status Label

status_label = tk.Label(

    root,

    text="Your Turn (X)",

    font=("Arial", 16),

    bg="#0f172a",

    fg="white"
)

status_label.pack(pady=20)

# Restart Button

restart_button = tk.Button(

    root,

    text="Restart Game",

    font=("Arial", 14, "bold"),

    bg="#2563eb",

    fg="white",

    relief="flat",

    padx=20,

    pady=10,

    cursor="hand2",

    command=restart_game
)

restart_button.pack(pady=10)

# Run App

root.mainloop()