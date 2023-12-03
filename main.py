import random
import time

def typing_game():
    words = ["python", "keyboard", "programming", "challenge", "speed", "practice", "improvement", "fun"]

    print("Welcome to the Typing Game!")
    input("Press Enter when you are ready...")

    while True:
        word = random.choice(words)
        print("\nType the word: ", word)

        start_time = time.time()
        user_input = input("Your input: ")

        end_time = time.time()
        elapsed_time = end_time - start_time

        if user_input.lower() == word:
            print(f"Correct! Time taken: {elapsed_time:.2f} seconds\n")
        else:
            print("Incorrect. Try again!\n")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    typing_game()
