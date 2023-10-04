import random

# Function to generate a random number between 'start' and 'end' (inclusive)


def generate_random_number(start, end):
    return random.randint(start, end)

# Function to get the player's guess (an integer)


def get_guess():
    while True:
        try:
            # Prompt the user for a guess and convert it to an integer
            return int(input("Guess the number: "))
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")

# Function to check if the guess matches the answer


def check_guess(guess, answer):
    return guess == answer

# Function to give a hint based on the guess compared to the answer


def give_hint(guess, answer):
    # Determine whether the answer is higher or lower than the guess
    hint = "higher" if guess < answer else "lower"
    print(f"The number is {hint} than your guess.")  # Provide the hint

# Function to play the game with a specified range of numbers


def play_game(start, end):
    # Generate a random answer within the given range
    answer = generate_random_number(start, end)
    score = 100  # Initialize the player's score

    while True:
        guess = get_guess()  # Get the player's guess
        if check_guess(guess, answer):
            # The guess matches the answer
            print("Congratulations! You guessed the number.")
            print("Your final score is:", score)  # Display the final score
            break
        else:
            give_hint(guess, answer)  # Provide a hint based on the guess
            score -= 10  # Deduct points for an incorrect guess


# Example usage
play_game(1, 100)  # Play the game with a range from 1 to 100
