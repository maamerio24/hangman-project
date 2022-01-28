import random
from words import wordlist

name = input("Enter your name: ")
print("Hello, " + name.title() + " let's play Hangman!")


def random_word():
    word = random.choice(wordlist)
    return word

def hangman():
    guessed_letters = []
    word_letters = []
    lives = 6
    done = False
    word = random_word()
   
    while not done and lives > 0:
        blank_word = [letter if letter in guessed_letters else '-' for letter in word]
        print("\nYour word is: ", " ".join(blank_word))
        print(f"You have {lives} lives left!")
        guess = input("Please guess a letter: ").upper()
    
        if guess not in word:
            print(guess + " is not in the word, please guess again. ")
            lives -= 1
            guessed_letters.append(guess)
        elif guess in word:
            print("Woohoo " + guess + " is in the word, keep guessing!")
            guessed_letters.append(guess)
        elif guess in guessed_letters:
            print("You have already guessed " + guess +
                  ", please guess a new letter. ")
        else:
            print("That is not a valid guess. Please guess again. ")
            
        

    else:
        again = input("\nSorry, you ran out of tries. Better luck next time! Would you like to play again? (Y/N) ").lower()
        if again == 'Y':
            hangman()
        if again == 'N':
            return


hangman()
