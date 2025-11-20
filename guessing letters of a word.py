# Get player's name and greet
import random
name = input("What is your name? ")
print("Good Luck!", name)

# List of possible words
words = ['Amrita', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Randomly select a word from the list
word = random.choice(words)
print("\nGuess the characters!")
print("7")
# Initialize variables
guesses = ''
max_wrong_guesses = 7 - 1
wrong_guesses = 0

# Main game loop
while wrong_guesses < max_wrong_guesses:
    failed = 0

    # Display the word with guessed letters and underscores for unguessed letters
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()  # New line after the word display

    # Check if the player has guessed the word
    if failed == 0:
        print("Congratulations, You Win!")
        print("The word is:", word)
        break



    # Get the user's guess
    guess = input("Guess a character: ").lower()

    # Add the guess to the guessed letters
    if guess not in guesses:
        guesses += guess

        # Check if the guessed character is not in the word
        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess.")
            print(f"You have {max_wrong_guesses - wrong_guesses} more guesses left.")
        else:
            print("Good guess!")

    else:
        print("You already guessed that letter. Try a different one.")

    # Check if no turns are left
    if wrong_guesses == max_wrong_guesses:
        print("You Lose! The word was:", word)
        break
