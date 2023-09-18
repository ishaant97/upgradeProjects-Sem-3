# Import the tkinter library for creating a GUI
from tkinter import *
import random

# Function to handle the next player's turn


def handle_turn(row, column):
    global current_player

    # Check if the button is empty and the game is not won
    if board[row][column]['text'] == "" and not check_winner():

        if current_player == players[0]:
            # Set the button's text to the current player's symbol (either 'X' or 'O')
            board[row][column]['text'] = current_player

            # Check for a winner
            if not check_winner():
                # Switch to the next player's turn
                current_player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                # Display a message if the current player wins
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                # Display a message for a tie game
                label.config(text="Tie!")
        else:
            board[row][column]['text'] = current_player

            if not check_winner():
                current_player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

# Function to check for a winner or a tie


def check_winner():
    # Check rows for a win
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            board[row][0].config(bg="green")
            board[row][1].config(bg="green")
            board[row][2].config(bg="green")
            return True

    # Check columns for a win
    for column in range(3):
        if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != "":
            board[0][column].config(bg="green")
            board[1][column].config(bg="green")
            board[2][column].config(bg="green")
            return True

    # Check diagonals for a win
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")
        return True
    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        board[0][2].config(bg="green")
        board[1][1].config(bg="green")
        board[2][0].config(bg="green")
        return True
    # Check for a tie
    elif no_empty_spaces():
        for row in range(3):
            for column in range(3):
                board[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False

# Function to check if there are any empty spaces left


def no_empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if board[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return True
    else:
        return False

# Function to start a new game


def start_new_game():
    global current_player

    # Randomly choose the starting player
    current_player = random.choice(players)

    # Update the label to indicate the starting player's turn
    label.config(text=current_player + " turn")

    # Clear the board
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", bg="#F0F0F0")


# Create the main window
window = Tk()
window.title("Tic-Tac-Toe")

# Define the two player symbols
players = ["X", "O"]
current_player = random.choice(players)

# Initialize the 3x3 grid of buttons
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Create a label to display the current player's turn
label = Label(text=current_player + " turn", font=('consolas', 40))
label.pack(side="top")

# Create a button to start a new game
new_game_button = Button(text="New Game", font=(
    'consolas', 20), command=start_new_game)
new_game_button.pack(side="top")

# Create a frame for the grid of buttons
frame = Frame(window)
frame.pack()

# Create the grid of buttons and attach the 'handle_turn' function to each button
for row in range(3):
    for column in range(3):
        board[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                    command=lambda row=row, column=column: handle_turn(row, column))
        board[row][column].grid(row=row, column=column)

# Start the main event loop
window.mainloop()
