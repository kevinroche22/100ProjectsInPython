##################
# Tip Calculator #
##################

## Intro
print("Welcome to the world's greatest tip calculator.")

## Determine the cost of the bill before tip
billBeforeTip = input("What amount did the bill come to? $")

## Determine tip percentage
tipPercentage = input("What percentage tip would you like to give? ")

## Determine the cost of the bill after tip
billAfterTip = round(
    float(billBeforeTip) * (1 + (float(tipPercentage) / 100)), 2
)

## Determine how many people are splitting the bill
numberOfPeopleSplitting = input("How many people are splitting the bill? ")

## Determine final cost per person
costPerPerson = round(float(billAfterTip) / int(numberOfPeopleSplitting), 2)

## Return calculations
print(
    f"After tip, the total bill comes to ${billAfterTip}. \
    Split {numberOfPeopleSplitting} ways, that comes out to ${costPerPerson}."
)

