import random

WORDS = ["python", "planet", "guitar", "castle", "rocket"]
MAX_WRONG = 6


def show_status(word, guessed, wrong_count):
    """Print the word with blanks, wrong guesses, and attempts left."""
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "none")
    print("Incorrect guesses left:", MAX_WRONG - wrong_count)


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong_count = 0

    print("=== HANGMAN ===")
    print("Guess the word one letter at a time. You can miss", MAX_WRONG, "times.")

    while wrong_count < MAX_WRONG:
        show_status(word, guessed, wrong_count)

        # Win check: every letter in the word has been guessed
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
        if won:
            print("\nYou won! The word was '" + word + "'.")
            return

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed '" + guess + "'. Try another.")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                wrong_count += 1
                print("Wrong! '" + guess + "' is not in the word.")

    print("\nGame over! The word was '" + word + "'.")


def main():
    play_again = "y"
    while play_again == "y":
        play()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
