
word = "PYTHON"
guessed_letters = set()

print("Welcome to Hangman!")
print("Guess the word letter by letter.")

while True:
    guess = input("Guess a letter: ").upper()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input! Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Good job! The letter is in the word.")
    else:
        print("Wrong letter!")

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break
