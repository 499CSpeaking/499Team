# ask the user for an input
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


# rock, paper, scissors ++++++++++++++++++++++++++++++++STARTS HERE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rockpaper():
    # Print selection options for the user inputs
    print("Welcome to Rock Paper Scissor!\nInput 1 for Rock , 2 for Paper , 3 for scissors!")
    # Take the users input
    inp = int(input("Make a selection: "))
    # Computer makes a random choice
    comp = random.randint(1,3)
    # if...elif statement to decide the winner and print it
    if (inp == comp): 
        print("Draw !!")
    elif (inp == 1 and comp == 2 ):
        print("Computer Wins")
    elif (inp == 1 and comp == 3):
        print("Player Wins")
    elif (inp == 2 and comp == 3 ):
        print("Computer Wins")
    elif (inp == 2 and comp == 1):
        print("Player Wins")
    elif (inp == 3 and comp == 1 ):
        print("Computer Wins")
    elif (inp == 3 and comp == 2):
        print("Player Wins")

# Rock, Paper, Scissors ++++++++++++++++++++++++++++++++ENDS HERE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# hangman
def hangman():
    print("Hello from a function")

# tic tac toe
def tictactoe():
    print("Hello from a function")

# call the main function
main()