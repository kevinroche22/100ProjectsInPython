#########################
# Rock, Paper, Scissors #
#########################

## Import packages
import random as rd
import time

## Declare variables
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

dynamite = """
 ___________________    . , ; .
(___________________|~~~~~X.;' .
                      ' `" ' `
            TNT
"""

## Prompt user
userChoice = input(
    'Welcome to stacked rock paper scissors, a game you\'ll surely lose as n approaches infinity. Enter either "rock", "paper", or "scissors" to play.\n'
)
time.sleep(  ## makes it seem like it's loading. incredible feature engineering on my end.
    0.5
)

## Define list of possible moves to be made by the CPU
computerChoiceList = ["rock", "paper", "scissors", "dynamite"]

## Computer randomly selects a move from outcomeList
computerChoice = rd.choice(computerChoiceList)

## Play game
if userChoice == "rock":
    print(f"\nYou chose rock:\n{rock}\n")
    if computerChoice == "rock":
        print(f"The computer chose rock:\n{rock}\nIt's a tie. Boring.")
    elif computerChoice == "paper":
        print(
            f"The computer chose paper:\n{paper}\nPaper covers rock. You return to your friends and family a failure."
        )
    elif computerChoice == "scissors":
        print(
            f"The computer chose scissors:\n{scissors}\nRock smashes scissors. Congratulations, buy a lottery ticket before your luck runs out."
        )
    else:
        print(
            f"The computer chose dynamite:\n{dynamite}\nDynamite blows up rock. A schoolyard classic. No one said this game was fair."
        )
elif userChoice == "paper":
    print(f"\nYou chose paper:\n{paper}\n")
    if computerChoice == "rock":
        print(
            f"The computer chose rock:\n{rock}\nPaper covers rock. Congratulations, buy a lottery ticket before your luck runs out."
        )
    elif computerChoice == "paper":
        print(f"The computer chose:\n{paper}\nIt's a tie. Boring.")
    elif computerChoice == "scissors":
        print(
            f"The computer chose scissors:\n{scissors}\nScissors cut paper. You return to your friends and family a failure."
        )
    else:
        print(
            f"The computer chose dynamite:\n{dynamite}\nDynamite incinerates paper. A schoolyard classic. No one said this game was fair."
        )
elif userChoice == "scissors":
    print(f"\nYou chose scissors:\n{scissors}\n")
    if computerChoice == "rock":
        print(
            f"The computer chose rock:\n{rock}\nRock smashes scissors. You return to your friends and family a failure."
        )
    elif computerChoice == "paper":
        print(
            f"The computer chose paper:\n{paper}\nScissors cut paper. Congratulations, buy a lottery ticket before your luck runs out."
        )
    elif computerChoice == "scissors":
        print(f"The computer chose scissors:\n{scissors}\nIt's a tie. Boring.")
    else:
        print(
            f"The computer chose dynamite:\n{dynamite}\nDynamite melts scissors. A schoolyard classic. No one said this game was fair."
        )
else:
    print(
        "\nInvalid move. In your defense, this is an incredibly complex game."
    )

