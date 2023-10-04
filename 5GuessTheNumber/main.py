import random


def generate_random_number(start, end):
    return random.randint(start, end)


def get_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_guess(guess, answer):
    if guess == answer:
        return True
    else:
        return False


def give_hint(guess, answer):
    if guess < answer:
        print("The number is higher than your guess.")
    else:
        print("The number is lower than your guess.")


def play_game(start, end):
    answer = generate_random_number(start, end)
    score = 100
    while True:
        guess = get_guess()
        if check_guess(guess, answer):
            print("Congratulations! You guessed the number.")
            print("Your final score is:", score)
            break
        else:
            give_hint(guess, answer)
            score -= 10


# example usage
play_game(1, 100)
