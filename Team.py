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
    print("Hello from a function")

# call the main function
main()