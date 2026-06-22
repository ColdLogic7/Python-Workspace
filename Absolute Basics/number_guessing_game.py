# 1. Pick a random number between 1 and 100
# 2. Ask the user to guess
# 3. Tell them: too high, too low, or correct
# 4. Count how many attempts they used
# 5. When correct — show the attempt count and ask to play again

import random

MAX_NUMBER = 100          # change this one line to make game harder/easier
MAX_ATTEMPTS = 7          # gives player a fair limit

def get_random_number():
    return random.randint(1,MAX_NUMBER) 
    # it's inclusive range like it included 1 and 100 both values, instead exclusive range which just include 99 not 100

def get_user_guess():
    while True:
        user_input = input("Your Guess: ").strip()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please Enter A Valid Number.")

def check_guess(guess, answer):
    if guess < answer:
        return "low"
    elif guess == answer:
        return "correct"
    else:
        return "high"

def play_game():
    answer = get_random_number()
    attempts = 0
    win = False

    while attempts < MAX_ATTEMPTS:
        guess = get_user_guess()
        attempts += 1

        result = check_guess(guess,answer)
        if result == 'correct':
            print(f"Correct! You Got It In {attempts} attempts")
            win = True
            break
        elif result == 'low':
            print("Too Low, try again")
        else:
            print("Too High, try again")

    if not win:
        print(f"You Lose, You Have No Attempts Left")

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
