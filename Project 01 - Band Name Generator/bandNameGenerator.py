#######################
# Band Name Generator #
#######################

## This program asks users their name. Once the user has given their name,
## the program returns a random two-word band name to the user in verb-noun format.

## Import packages
from random_word import RandomWords

r = RandomWords()

## Generate band name
print(
    input("What is your name? ")
    + ", your band name is "
    + r.get_random_word(
        hasDictionaryDef="true",
        includePartOfSpeech="verb",
        minLength=5,
        maxLength=10,
        minCorpusCount=5,
        minDictionaryCount=5,
    )
    + " "
    + r.get_random_word(
        hasDictionaryDef="true",
        includePartOfSpeech="noun",
        minLength=5,
        maxLength=10,
        minCorpusCount=5,
        minDictionaryCount=5,
    )
)

