"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    print("""
    ------------------------------------
    Welcome to the Number Guessing Game!
    ------------------------------------
    """)
    correct_number = random.randint(1,10)
    attempts = 0
    while True:
        try:
            guessed_number = int(input("Pick a number between 1 and 10: "))
            if guessed_number < 1 or guessed_number > 10:
                print("Please enter a number between 1 and 10")
                continue
        except ValueError:
            print("Oh no, we ran into an issue. Please enter a number.")
        else:
            if guessed_number == correct_number: 
                attempts += 1  
                print("Got it. It took you {} tries.".format(attempts))
                break
            elif guessed_number > correct_number:
                attempts += 1  
                print("It's lower")
                continue
            elif guessed_number < correct_number:
                attempts += 1  
                print ("It's higher")
                continue
    
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.lower() == "y":
        print("The HIGHSCORE is {}".format(attempts))
        start_game()
    else:       
        print("Closing game, See you next time!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
