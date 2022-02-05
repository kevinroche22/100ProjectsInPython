#################
# Caesar Cipher #
#################

## Supply list of alphabet
from alphabet import alphabet

## Define encyption function
def caesarCipher(message, shift):

    ## Create empty encrypted message
    encryptedMessage = ""

    ## Create empty decrypted message
    decryptedMessage = ""

    if codeType == "encode":

        ## Shift phrase
        for i in message:
            if i in alphabet:
                index = alphabet.index(i)
                newPosition = index + shift
                newLetter = alphabet[newPosition]
                encryptedMessage += newLetter
            else:
                encryptedMessage += i

        ## Print encrypted message
        print(f"Your encrypted message is {encryptedMessage}.")

    elif codeType == "decode":

        ## Shift phrase
        for i in message:
            if i in alphabet:
                index = alphabet.index(i)
                newPosition = index - shift
                newLetter = alphabet[newPosition]
                decryptedMessage += newLetter
            else:
                decryptedMessage += i

        ## Print encrypted message
        print(f"Your decrypted message is {decryptedMessage}.")

    else:

        ## Return error
        print("Invalid entry - please enter 'encode or 'decode'.")

## Initialize reRun option
reRun = "yes"

## Run program
while reRun != "no":

    ## Prompt user to encode or decode
    codeType =  input("Enter 'encode' to encrypt, or 'decode' to decrypt:\n")

    ## Prompt user for message
    message = input("Enter your message:\n").lower()

    ## Prompt user for size of shift
    shift = int(input("Enter how many letters you'd like to shift your message:\n")) % 26

    ## Return encrypted or decrypted decrypted message
    caesarCipher(message, shift)

    ## Prompt user to re-run
    reRun = input("Re-run the encryption? Enter 'yes' or 'no'.\n")
