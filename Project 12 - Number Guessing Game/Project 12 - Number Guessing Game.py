########################
# Number Guessing Game #
########################

## Import packages
from random import randint as rd

## Print opening statement
print("Welcome to the number guessing game. I've chosen a number between 0 and 100. Your goal is to guess the number in either 5 guesses (hard mode) and 10 guesses (easy mode). After each guess, I'll let you know if your guess was too high or too low.\nLet's begin.")

## Generate number
correctNumber = rd(0, 100)

## Initialize victory variable
victory = False

## Prompt user for game mode
gameMode = input("Enter 'easy' to play on easy mode or 'hard' to play on hard mode.")

## Assign number of guesses based on game mode
if gameMode != "easy" and gameMode != "hard":

    while gameMode != "easy" and gameMode != "hard":

        print("Invalid input.")

        gameMode = input("Enter 'easy' to play on easy mode or 'hard' to play on hard mode.")

if gameMode == "easy":

    numberOfGuesses = 10

if gameMode == "hard":

    numberOfGuesses = 5

## Define guess function
def guess(currentGuess):

    global numberOfGuesses

    global victory

    if currentGuess > correctNumber:

        print("Too high.")

        numberOfGuesses -= 1

    elif currentGuess < correctNumber:

        print("Too low.")

        numberOfGuesses -= 1

    else:

        victory = True

## Play game
while numberOfGuesses > 0:

    if victory == False:

        currentGuess = int(input(f"You have {numberOfGuesses} guesses left. Guess a number."))

        guess(currentGuess)

    else:

        print(f"You won with {numberOfGuesses} guesses remaining!")

        numberOfGuesses = 0

if victory == False:

    print(f"You lost! The correct number was {correctNumber}.")
