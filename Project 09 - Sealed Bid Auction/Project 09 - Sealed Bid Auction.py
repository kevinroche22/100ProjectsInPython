##################################
# First-price Sealed Bid Auction #
##################################

## Import packages
import os

## Initialize empty dictionary
bidDict = {}

## Initialize other bidders
otherBidders = "yes"

## Write function to determine highest bidders
def highestBidder(bidDict):
    highestBid = 0
    highestBidder = ""
    tie = []
    for bidder in bidDict:
        currentBid = bidDict[bidder]
        if currentBid > highestBid:
            highestBid = currentBid
            highestBidder = bidder.capitalize()
            tie = []
            tie.append(bidder.capitalize())
        elif currentBid == highestBid:
            tie.append(bidder.capitalize())
    if len(tie) > 1:
        print("There\'s been a tie! " + " & ".join([str(x) for x in tie]) + " need to bid again. All other bidders have been eliminated.")
    else:
        print(f"The winner is {highestBidder} with a bid of ${highestBid}.")

while otherBidders != "no":

    ## Prompt user for their name
    name = input("What is your name?\n").lower()

    ## Prompt user for bid
    bid = int(input("What are you willing to bid?\n"))

    ## Add name and bid to dictionary
    bidDict[name] = bid

    ## Prompt user about other bidders
    otherBidders = input("Are there any other bidders? Enter 'yes' to continue, or 'no' to unveil winner.\n")

    ## Clear screen
    os.system('clear')

    ## Declare winner
    if otherBidders == "no":

        ## Declare highest bidder
        winner = str(highestBidder(bidDict))

        ## Check if tie
        if winner.find("tie"):

            ## If tie start again
            otherBidders == "yes"
