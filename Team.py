import random

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
    print("4. Three Cup Monte")
    print("5. Exit")
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
    # if they want to play three cup monte
    elif game == "4":
        threecup()
    # if they want to exit
    elif game == "5":
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

# three cup monte
def threecup():
    ball = random.randint(1,3)
    if ball == 1:
        print(" /\\"+" "+"  /\\"+" "+"  /\\"
        +"\n"+"/"+str(ball)+" \\"+" "+"/  \\"+" "+"/  \\")
    elif ball == 2:
        print(" /\\"+" "+"  /\\"+" "+"  /\\"
        +"\n"+"/  \\"+" "+"/"+str(ball)+" \\"+" "+"/  \\")
    elif ball == 3:
        print(" /\\"+" "+"  /\\"+" "+"  /\\"
        +"\n"+"/  \\"+" "+"/  \\"+" "+"/"+str(ball)+" \\")
    print("ball is in cup #"+str(ball))
    ball = random.randint(1,3)
    print("the cups are shuffled!")
    ball = random.randint(1,3)
    print(" /\\"+" "+"  /\\"+" "+"  /\\"
        +"\n"+"/ \\"+" "+"/  \\"+" "+"/  \\")
    print("Guess which cup its in: 1, 2 or 3?")
    guess = input()
    if int(guess) == ball:
        print("You win!")
    else:
        print("You lose! Hold that L")

# call the main function
main()