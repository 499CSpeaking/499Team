# ask the user for an input

# import random
import random

def main():
    # ask the user for an input
    print("What is your name?")
    name = input()
    # which game/program do they want to do?
    print("What game do you want to play?")
    print("1. Rock, Paper, Scissors")
    print("2. Hangman")
    print("3. Tic Tac Toe")
    print("4. Exit")
    game = input()
    # if they want to play rock, paper, scissors
    if game == "1":
        rockpaper()
    # if they want to play hangman
    elif game == "2":
        hangman()
    # if they want to play tic tac toe
    elif game == "3":
        tictactoe()
    # if they want to exit
    elif game == "4":
        exit()


# rock, paper, scissors
def rockpaper():
    print("Hello from a function")

# hangman


def hangman():
    print("Hello from a function")

# tic tac toe


def tictactoe():
    print("Player1, [C]omputer or [H]uman?")
    player1 = input()
    print("Player2, [C]omputer or [H]uman?")
    player2 = input()
    # setup the blank board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    # if player1 is human
    playerTurn(player1, player2, board)


def playerTurn(player1, player2, board):
    printBoard(board)

    if player1 == "H":
        print("Player1, what is your move?")
        move = input()
        # check if the space is empty
        while board[int(move)] != " ":
            print("That space is already taken")
            print("Player2, what is your move?")
            move = input()
        board[int(move)] = 'X'

    else: computermove('X', board)
    printBoard(board)

    if player2 == "H":
        print("Player2, what is your move?")
        move = input()
        # check if the space is empty in a while loop
        while board[int(move)] != " ":
            print("That space is already taken")
            print("Player2, what is your move?")
            move = input()
        board[int(move)] = 'O'

    else: computermove('O', board)
    playerTurn(player1, player2, board)

def computermove(char, board):
        # check if the space is empty in a while loop
        move = random.randint(0, 8)
        while board[move] != " ":
            move = random.randint(0, 8)
        board[move] = char

def printBoard(board):
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")
    checkwin(board)


def checkwin(board):
    # check for a win
    if(board[4] == board[0] == board[8]
    or board[4] == board[2] == board[6]
    or board[4] == board[1] == board[7]
    or board[4] == board[3] == board[5]
    or board[0] == board[1] == board[2]
    or board[6] == board[7] == board[8]
    or board[0] == board[3] == board[6]
    or board[2] == board[5] == board[8]):
       print ("You win!")
    
    
    
    
           


    # call the main function
main()
