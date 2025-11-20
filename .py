import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Guess must be between 1 and 100!")
                continue

            if guess == number:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
            elif abs(guess - number) <= 5:
                print("🔥 Very Close!")
            elif guess > number:
                print("📉 Too High!")
            else:
                print("📈 Too Low!")

        except ValueError:
            print("⚠️ Please enter a valid number!")

# Run the game
number_guessing_game()
