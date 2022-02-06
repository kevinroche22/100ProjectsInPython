##############
# Calculator #
##############

## Import functions
from calcFunctions import *

## Define recursive calculator function
def calculator():

    ## Prompt user to enter inputs
    firstNumber = int(input("Enter your first number."))
    for i in operationsDictionary:
        print(i)
    operation = input("Which of the above operations would you like to perform?")

    ## Calculate answer
    if operation not in operationsDictionary:

        ## Ensure operation is in dictionary
        while operation not in operationsDictionary:

            print("Invalid entry.")

            operation = input("Please enter a valid operation.")

    ## Prompt user for second number
    secondNumber = int(input("Enter your second number."))

    ## If operaiton is in dictionary, calculate answer
    answer = operationsDictionary[operation](firstNumber, secondNumber)

    ## Return answer
    print(f"{firstNumber} {operation} {secondNumber} = {answer}")

    ## Prompt user to continue
    moreCalculations = input("Would you like to make additional calculations on the answer? Enter \"yes\" or \"no\".")

    if moreCalculations != "yes" and moreCalculations != "no":

        while moreCalculations != "yes" and moreCalculations != "no":

            print("Invalid entry. Please enter 'yes' or 'no'.")

            ## Prompt user to continue
            moreCalculations = input("Would you like to make additional calculations on the answer? Enter \"yes\" or \"no\".")

    elif moreCalculations == "yes":

        while moreCalculations != "no":

            ## Prompt user to enter inputs
            for i in operationsDictionary:
                print(i)
            operation = input("Which of the above operations would you like to perform on the answer?")
            newNumber = int(input("Enter your new number."))

            ## Calculate answer
            newAnswer = operationsDictionary[operation](answer, newNumber)

            ## Return answer
            print(f"{answer} {operation} {newNumber} = {newAnswer}")
            answer = newAnswer

            ## Prompt user to continue
            moreCalculations = input("Would you like to make additional calculations on the answer? Enter \"yes\" or \"no\".")

    newCalculation = input("Would you like to make a new calculation?")

    if newCalculation != "yes" and moreCalculations != "no":

        while moreCalculations != "yes" and moreCalculations != "no":

            print("Invalid entry. Please enter 'yes' or 'no'.")

            ## Prompt user to continue
            newCalculation = input("Would you like to make additional calculations? Enter \"yes\" or \"no\".")

    elif newCalculation == "yes":

        calculator()

    elif newCalculation == "no":

        return "Thanks for using the calculator. Cheers!"

calculator()
