import random


def get_guess():
    """Get a valid whole number between 1 and 100."""

    while True:
        text = input("Enter your guess (1-100): ").strip()

        try:
            guess = int(text)

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if 1 <= guess <= 100:
            return guess

        print("Your guess must be between 1 and 100.")


def play_round():
    """Play one round and return the number of attempts."""

    secret = random.randint(1, 100)
    attempts = 0

    print("\nI have picked a number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low! Try a higher number.")

        elif guess > secret:
            print("Too high! Try a lower number.")

        else:
            print(f"Correct! The number was {secret}.")
            print(f"You guessed it in {attempts} attempt(s).")
            return attempts


def main():
    print("Welcome to the Number Guessing Game!")

    best_score = None

    while True:
        attempts = play_round()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New best score!")

        print(f"Best score so far: {best_score} attempt(s)")

        again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if again in ("yes", "y"):
            continue

        print("Thank you for playing!")
        break


if __name__ == "__main__":
    main()