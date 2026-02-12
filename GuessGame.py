import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    while guess < 1 or guess > difficulty:
        print(f"Invalid number . Please choose a number between 1 and {difficulty}.")
        guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    return guess


def compare_results(guess, secret_number):
    if guess == secret_number:
        return True
    return False


def play(difficulty):
    guess = get_guess_from_user(difficulty)
    secret_number = generate_number(difficulty)
    return compare_results(guess, secret_number)