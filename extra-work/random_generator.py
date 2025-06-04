import random

while True:
    secret_number = random.randint(1, 10)
    print("Welcome to the random number guessing game!")
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye. 👋")
        break
