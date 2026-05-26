import math
import random 
import time

print("-----------------Choose a game!-----------------")


def game_caesar():
    def caesar(text, shift, encrypt=True):
        if not isinstance(shift, int):
            return 'Shift must be an integer value.'

        if shift < 1 or shift > 25:
            return 'Shift must be an integer between 1 and 25.'

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        if not encrypt:
            shift = -shift

        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        translation_table = str.maketrans(
            alphabet + alphabet.upper(),
            shifted_alphabet + shifted_alphabet.upper()
        )
        return text.translate(translation_table)

    operation = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    input_text = input("Enter the text to process: ")

    try:
        input_shift = int(input("Enter the numerical shift key (1-25): "))
    except ValueError:
        print("\nInvalid shift key. Using a default shift of 3.")
        input_shift = 3

    if operation == 'E':
        print(f"\nEncrypted Message: {caesar(input_text, input_shift)}")
    elif operation == 'D':
        print(f"\nDecrypted Message: {caesar(input_text, input_shift, encrypt=False)}")
    else:
        print("\nInvalid operation.")

def numb_guess():

    import random
    tries = 0
    number = random.randint(1, 100)

    while True:
        guess_input = input("Guess a number between 1 and 100: ")

        try:
            guess = int(guess_input)
        except ValueError:
            print("Please type a number.\n")
            continue

        tries += 1

        if guess > number:
            print("Too high!\n")
        elif guess < number:
            print("Too low!\n")
        else:
            print(f"Correct! It took you {tries} tries!\n")
            break

def game_even_odd():
    while True:
        try:
            number = int(input("Enter a number to check if it's even or odd: "))
            if number % 2 == 0:
                print(f"{number} is even.\n")
            else:
                print(f"{number} is odd.\n")
            break
        except ValueError:
            print("Please enter a valid integer (A number).\n")

def game_of_pig(): 
    total_score = 0
    computer_score = 0
    turn_number = 1
    roll = random.randint(1, 6)

    while total_score < 100 and computer_score < 100:
        # --- PLAYER TURN ---
        round_score = 0
        turn_active = True
        
        print(f"Turn {turn_number}")
        print(f"Your Total Score: {total_score}")
        print(f"Computer Total Score: {computer_score}")
        
        while turn_active:
            print(f"Current round points: {round_score}\n")
            choice = input("Would you like to roll or bank? ").strip().lower()
            
            if choice == 'bank':
                if round_score == 0:
                    print("Are you sure? ")
                total_score += round_score
                turn_active = False
                print(f"Banked! Your total score is now {total_score}.\n")
            elif choice == 'roll':
                roll = random.randint(1, 6)
                print(f"You rolled a {roll}.")
                if roll == 1:
                    round_score = 0
                    turn_active = False
                    print("Ouch! Rolled a 1. Zero points this round.\n")
                else:
                    round_score += roll
            else:
                print("Invalid input. Please type 'roll' or 'bank'.")

        # --- COMPUTER TURN ---
        # Only plays if player hasn't already reached 100
        if total_score < 100:
            print("Computer's turn")
            comp_round_score = 0
            comp_turn_active = True
            
            while comp_turn_active:
                # Logic: Roll if round score <= 15
                if comp_round_score <= 15:
                    roll = random.randint(1, 6)
                    print(f"Computer rolled a {roll}.")
                    
                    if roll == 1:
                        comp_round_score = 0
                        comp_turn_active = False
                        print("Computer rolled a 1! No points gained.\n")
                    else:
                        comp_round_score += roll
                        print(f"The round the computer has: {comp_round_score}")
                        print("The computer chooses to roll again.\n")
                    
                else:
                    # Bank if round score > 15
                    computer_score += comp_round_score
                    comp_turn_active = False
                    print(f"Computer banks {comp_round_score} points.\n")
            
        turn_number += 1

    # --- END GAME ---
    print("FINAL SCORE:")
    print(f"Player: {total_score} | Computer: {computer_score}")

    if total_score > computer_score:
        print("Congratulations! You won!")
    elif computer_score > total_score:
        print("The computer won. Better luck next time!")
    else:
        print("It's a tie!")
#BETA!!!
def cord_diff():
    def distance(first_point, second_point):
        x_diff = second_point[0] - first_point[0]
        y_diff = second_point[1] - first_point[1]
        sum_of_squares = pow(x_diff, 2) + pow(y_diff, 2)
        return math.sqrt(sum_of_squares)

    print("Enter coordinates as x, y (e.g., 3, 4): ")
    p1_input = input("Point 1: ").split(",")
    p2_input = input("Point 2: ").split(",")

    point1 = (int(p1_input[0]), int(p1_input[1]))
    point2 = (int(p2_input[0]), int(p2_input[1]))

    result = distance(point1, point2)
    rounded = round(result, 3)
    print(f"The distance is: {rounded}")

def tic_tac_toe():
        
    def get_valid_index(prompt):
        while True:
            try:
                index = int(input(prompt))
                index -= 1
                if index >= 0 and index <= 2:
                    return index
                print("Must be 0 - 2 inclusive!")
            except ValueError:
                print("Must be an integer!")

    def game_is_over(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
                print_board(board)
                print(board[i][0] + " wins!")
                return True
            
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
                print_board(board)
                print(board[0][i] + " wins!")
                return True
            
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            print_board(board)
            print(board[0][0] + " wins!")
            return True
        
        if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
            print_board(board)
            print(board[2][0] + " wins!")
            return True
        
        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            print_board(board)
            print("Tie game!")
            return True
        
        return False
        
    def print_board(board):
        for row in board:       
            print(row)

    board = [                   
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    turn = "x"
    while not game_is_over(board):
        print_board(board)
        print("\nIt's " + turn + "'s turn.")
        row = get_valid_index("\n\nRow: ")
        col = get_valid_index("\nCol: ")
        print("\n")
        

        if board[row][col] != " ":
            print("That space is taken!")
        else:
            board[row][col] = turn
            if turn == "x":
                turn = "o"
            else:
                turn = "x"

def post_game_menu():
    time.sleep(5)
    print("\nWhat would you like to do next?\n")
    print("(1) Play the same game again\n")
    print("(2) Choose a different game\n")
    print("(3) End the game\n")
    return input("Enter 1, 2, or 3: ").strip()

def game_choice():
    last_game = None

    while True:
        if last_game is None:
            user_input = input(
                "(1.) Caesar Encryptor\n"
                "(2.) Number Guessing\n"
                "(3.) Even or Odd\n" \
                "(4.) Game of Pigs\n" \
                "(5.) Coordinate Difference\n"
                "(6.) Tic Tac Toe\n\n"
                "Enter the number: ").strip().lower()

            if user_input in ["1", "one"]:
                print("\nYou have chosen the Encrypting/Decrypting game!\n")
                last_game = game_caesar

            elif user_input in ["2", "two"]:
                print("\nYou have chosen the Number Guessing game!\n")
                last_game = numb_guess

            elif user_input in ["3", "three"]:
                print("\nYou have chosen the Even or Odd game!\n")
                last_game = game_even_odd
            elif user_input in ["4", "four"]:
                print("\nYou have chosen the Game of Pigs!" )
                last_game = game_of_pig
            elif user_input in ["5", "five"]:
                print("\nYou have chosen the Coordinate difference!" )
                last_game = cord_diff
            elif user_input in ["6", "six"]:
                last_game = tic_tac_toe

                

            else:
                print("Invalid choice!")
                continue


        last_game()

        choice = post_game_menu()

        if choice == "1":
            continue

        elif choice == "2":
            last_game = None
            continue

        elif choice == "3":
            print("Thanks for playing!")
            break

        else:
            print("Invalid input. Ending game.")
            break

game_choice()

#this is me testing the commit feature of git, ignore this comment.