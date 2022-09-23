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
    # this function is to return the target word only including guessed letters
    def incomplete_word(target_word, selected_letters):
        buffer = ""
        for letter in target_word:
            if letter == " " or letter in selected_letters:
                buffer += (letter + ",")
            else:
                buffer += "_,"
        
        return buffer
    
    # check if the user guessed all the letters
    def guessed_all_letters(word, guessed_letters):
        for letter in word:
            if letter != " " and letter not in guessed_letters:
                return False
        return True

    #choose the target word
    words = [
        "apple",
        "perry the platypus",
        "orange",
        "big chungus",
        "this is a sentance",
        "python is a nice language",
        "running out of ideas",
        "why ya spill yer beans"
    ]
    target_word = random.choice(words)
    
    #this object will keep track of the letters the user chose
    selected_letters = set()

    #number of wrong moves the user gets to guess the word
    tries_left = 3

    #game loop
    while(True):
        print(incomplete_word(target_word, selected_letters))
        if guessed_all_letters(target_word, selected_letters):
            print("you won!")
            break

        if tries_left <= 0:
            print("you suck")
            break

        print(f"{tries_left} incorrect guesses left")

        print("") #newline
        user_input = input()
        if len(user_input) != 1 or not user_input[0].isalpha():
            print("invalid input")
            continue

        user_letter = user_input[0]
        if user_letter in selected_letters:
            print("you already guessed that letter")
            continue
        
        selected_letters.add(user_letter)
        #if the letter is correct
        if user_letter in target_word:
            pass
        else:
            tries_left -= 1

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
    if ((board[4] == board[0] == board[8]) and board[4] != " "
    or (board[4] == board[2] == board[6]) and board[4] != " "
    or (board[4] == board[1] == board[7]) and board[4] != " "
    or (board[4] == board[3] == board[5]) and board[4] != " "
    or (board[0] == board[1] == board[2]) and board[0] != " "
    or (board[6] == board[7] == board[8]) and board[6] != " "
    or (board[0] == board[3] == board[6]) and board[0] != " "
    or (board[2] == board[5] == board[8])):
       print("You win!")
    
    
    
    
           



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

