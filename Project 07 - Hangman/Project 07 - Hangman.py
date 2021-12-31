###########
# Hangman #
###########

## Import packages
import random as rd
from hangmanArt import stages, logo
from hangmanWordList import wordList

## Choose a random word from the word list and save its length
chosenWord = rd.choice(wordList)
wordLength = len(chosenWord)

## Define initial parameters
endOfGame = False
lives = 6

## Print logo
print(logo)

## Create blanks
display = []
for i in range(wordLength):
    display += "_"

## Play game
while not endOfGame:

    ## Ask user to input their guess and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    ## Let user know if they've already guessed that letter
    if guess in display:
      print("You've already guessed that letter, try again.")

    ## Check if guessed letter is in word and update display accordingly
    for i in range(wordLength):
        letter = chosenWord[i]
        if letter == guess:
            display[i] = letter

    ## Check if user is wrong
    if guess not in chosenWord:
        print("That letter isn't in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose.")

    ## Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    ## Check if user has won the game
    if "_" not in display:
        end_of_game = True
        print("You win.")

    ## Print hangman graphic
    print(stages[lives])
