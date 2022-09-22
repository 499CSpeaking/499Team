# ask the user for an input


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
    print("Hello from a function")

# call the main function
main()