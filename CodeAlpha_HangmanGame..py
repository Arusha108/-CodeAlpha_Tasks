import random
# Define a list of 5 words
words = ["apple", "banana", "grape", "orange", "melon"]
#Pick a random word
word = random.choice(words)
# Create a blank version of the word
guessed_word = ["_"] * len(word)
attempts_left = 6
guessed_letters = []
# Start the game loop
while attempts_left > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Attempts left:", attempts_left)

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
        print("Correct!")
    else:
        attempts_left -= 1
        print("Wrong guess.")

# End of game message
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nSorry! You're out of attempts. The word was:", word)
