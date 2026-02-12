from CurrencyRouletteGame import play as currplay
from GuessGame import play as guessplay
from MemoryGame import play as memplay
from Score import add_score

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print(
        '''
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
         '''
    )
    game_choice = int(input("Enter the game number you want to play (1-3): "))
    while game_choice not in [1, 2, 3]:
        game_choice = int(input("Invalid input. Please enter a valid game number (1-3): "))

    difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
    while difficulty_level not in [1, 2, 3, 4, 5]:
        difficulty_level = int(input("Invalid input. Please enter a valid difficulty level (1-5): "))

    if game_choice == 1:
        game_won = memplay(difficulty_level)
    elif game_choice == 2:
         game_won = guessplay(difficulty_level)
    else:
        game_won = currplay(difficulty_level)

    # return game_choice, difficulty_level

    if game_won:
        add_score(difficulty_level)

load_game()