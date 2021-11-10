#############################
# Choose Your Own Adventure #
#############################

## High quality art
print(
    """
                 -|
               -' |
             -'   | __().
        ==wkm=====|'\/   `.O__
                            \ `,
                           _-^.
                           `.  `---,
                             :



       ____________________________________
       ///\\\///\\\///\\\///\\\///\\\///\\\
"""
)

## Intro
print(
    "\nYou wake up in a high-end condo in Toronto. You don't remember how you got here, but you know it's not yours."
)
print(
    "You get up and work your way over to the bathroom, where you look in the mirror. It's not you staring back at you in your reflection.\n\nIt's Masai Ujiri."
)
print(
    "\nYou quickly realize you're in a freaky friday style situation, and decide to forgo all further character development by comitting to a simple goal that will require some if-else statements: Make a series of trades that will bring the Toronto Raptors another championship.\n"
)

## Yes, this is really just an elaborate roast of James Dolan. Poor knicks fans.
dolanTrade = input(
    "As if on cue, the phone rings. It's James Dolan, owner of the Knicks and world-renowned moron. He offers up Kemba Walker and two tickets to see his band (his show didn't sell out; shocker) for Scottie Barnes, the Raptors unproven rookie. Do you take the trade? (Y/N) "
)

if dolanTrade == "Y":
    print(
        "\nYou fool. You spend the rest of eternity front row at a James Dolan concert. All of the instruments are out of tune, and he plays Pearl Jam on repeat. Start over."
    )
elif dolanTrade == "N":
    surpriseCall = input(
        "\nYou hang up the phone knowing you dodged a bullet. Before you're able to step away from the receiver (I'm not sure why I'm acting like corded phones are still a thing, but just run with it), it rings again. Do you answer? (Y/N) "
    )
    if surpriseCall == "Y":
        lunchWithJenny = input(
            "\nIt's Jennifer Anniston. She'd like to grab lunch this afternoon. Are you in? (Y/N) "
        )
        if lunchWithJenny == "Y":
            print(
                "\nI, the author breaking the fourth wall, don't blame you for saying yes. But it's not Jennifer Anniston waiting for you at lunch when you arrive, it's James Dolan. He hypnotizes you, and you spend the rest of eternity front row at one of his concerts. All of the instruments are out of tune, and he plays Pearl Jam on repeat. Start over."
            )
        else:
            print(
                "\nGood call, it was definitely that damn James Dolan trying to trick you. I'm bored now, so the rest of the story proceeds as follows: as GM of the Raptors, you decide not to make any moves. Scottie Barnes leads you to the championship, and you return to your everyday life with a story no one will ever believe. Congratulations, you win, I guess."
            )
    else:
        print(
            "\nUh-oh, Shaq attack! Entirely unprovoked, Shaq breaks into your apartment and, for the first time in his career, lands a punch. He hits you so hard that you return to your normal body with no championship. Start over."
        )

