######################
# Password Generator #
######################

## Import packages
import secrets as sc
import random as rd

## Define parameters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

## Initialize empty password list
passwordList = []

## Get inputs
print("Welcome to the Kev's Password Generator! Let's get started.")
nLetters= int(input("How many letters would you like in your password?\n"))
nSymbols = int(input(f"How many symbols would you like?\n"))
nNumbers = int(input(f"How many numbers would you like?\n"))

## Generate password characters
for i in range(nLetters):
    passwordList += sc.choice(letters)

for i in range(nSymbols):
    passwordList += sc.choice(symbols)

for i in range(nNumbers):
    passwordList += sc.choice(numbers)

## Shuffle password characters
rd.shuffle(passwordList)

## Convert to string and join characters with no space inbetween
password = ''.join(map(str, passwordList))

## Return password
print(f"Your new password is {password}")
