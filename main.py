import random


def play_game():
    """Main function to run the Hangman word guessing game."""
    # List of 5 predefined words
    word_list = ["python", "computer", "college", "coding", "developer"]

    # Randomly select a secret word from the list
    secret_word = random.choice(word_list)

    # List to store all letters guessed by the player
    guessed_letters = []

    # Maximum number of incorrect guesses allowed
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    print("=" * 45)
    print("      WELCOME TO CODEALPHA HANGMAN GAME      ")
    print("=" * 45)
    print("Rules:")
    print("- Guess the secret word one letter at a time.")
    print(f"- You are allowed a maximum of {max_incorrect_guesses} incorrect guesses.")
    print("=" * 45)

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build the current display representation of the secret word
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        # Display current word status and remaining attempts
        print("\nWord: " + " ".join(display_word))
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check if the player has guessed all letters correctly
        if "_" not in display_word:
            print("\n" + "*" * 45)
            print(f"CONGRATULATIONS! You won! The word was: '{secret_word}'")
            print("*" * 45)
            break

        # Ask user for input
        guess = input("Enter a letter: ").strip().lower()

        # Input validation: Ensure the user enters exactly one alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("[!] Invalid input! Please enter a single alphabetic letter (a-z).")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"[!] You have already guessed '{guess}'. Try a different letter.")
            continue

        # Add guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"[+] Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"[-] Wrong guess! '{guess}' is not in the word.")

    # Game over condition if player ran out of attempts
    if incorrect_guesses >= max_incorrect_guesses:
        print("\n" + "=" * 45)
        print("GAME OVER! You ran out of guesses.")
        print(f"The correct word was: '{secret_word}'")
        print("=" * 45)


if __name__ == "__main__":
    play_game()
