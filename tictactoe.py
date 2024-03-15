import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Represents the Tic-Tac-Toe board
player = 1  # Player indicator, Player 1 starts

# Game status flags
Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running  # Initially, the game is running
Mark = 'X'  # Mark used for Player 1


def DrawBoard():
    # Function to draw the Tic-Tac-Toe board
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")


def CheckPosition(x):
    # Function to check if a position on the board is available
    if board[x] == ' ':
        return True
    else:
        return False


def CheckWin():
    # Function to check if a player has won the game
    global Game

    # Check all possible winning combinations
    if (board[1] == board[2] == board[3] != ' ') or \
            (board[4] == board[5] == board[6] != ' ') or \
            (board[7] == board[8] == board[9] != ' ') or \
            (board[1] == board[4] == board[7] != ' ') or \
            (board[2] == board[5] == board[8] != ' ') or \
            (board[3] == board[6] == board[9] != ' ') or \
            (board[1] == board[5] == board[9] != ' ') or \
            (board[3] == board[5] == board[7] != ' '):
        Game = Win  # If any winning condition is met, set Game to Win
    elif all(x != ' ' for x in board[1:]):  # If all positions are filled and no winner, it's a draw
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game Designed By Sourabh Somani")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)

while Game == Running:
    os.system('cls')  # Clear the console
    DrawBoard()  # Draw the current board

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    if CheckPosition(choice):
        board[choice] = Mark  # Mark the chosen position
        player += 1  # Increment player
        CheckWin()  # Check if someone has won or the game is drawn

    os.system('cls')  # Clear the console
    DrawBoard()  # Draw the current board

    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1  # Adjust player count
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
