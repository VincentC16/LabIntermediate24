import random

wins = 0
losses = 0

def hangman(word_list):
    global wins, losses

    while word_list:
        word = random.choice(word_list)
        word_list.remove(word)
        guessed_letters = set()
        guesses = 9

        print("Welcome to Hangman!")
        print("Guess the word letter by letter.")

        while guesses > 0:
            display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
            print("Current word:", display_word)

            if "_" not in display_word:
                print("\nCongratulations! You guessed the word:", word)
                wins += 1
                break

            guess = input("Guess a letter or type 'QUIT' to exit: ").upper()

            if guess == "QUIT":
                print("\nFinal Score - Wins:", wins, "Losses:", losses)
                return

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
                guesses -= 1
                print("You have", guesses, "guesses left.")

        if guesses == 0:
            print("\nGame over! You ran out of guesses. The word was:", word)
            losses += 1

        print("\nCurrent Score - Wins:", wins, "Losses:", losses)

        if not word_list:
            print("No more words left! Thanks for playing!")
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nFinal Score - Wins:", wins, "Losses:", losses)
            break

secret_words = ["PYTHON", "COMPUTER", "LAPTOP", "ONLINE"]

temp_words = secret_words[:]
hangman(temp_words)