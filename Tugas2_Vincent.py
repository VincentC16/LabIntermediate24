
word = "QWERTY"
guessed_letters = set()
guesses = 6

print("Welcome to Hangman!")
print("Guess the word letter by letter.")

while guesses != 0:
    guess = input("Guess a letter: ").upper()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input! Please enter a single letter.")
        guesses = guesses - 1
        print("You have ",guesses," left")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Good job! The letter is in the word.")
        guesses = guesses - 1
        print("You have ",guesses," left")
    else:   
        print("Wrong letter!")
        guesses = guesses - 1
        print("You have ",guesses," left")

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

if guesses == 0 and not all(letter in guessed_letters for letter in word):
    print("Gameover, You ran out of guesses!")
    print("The word is",word)