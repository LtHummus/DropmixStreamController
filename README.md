# DropmixStreamController
A quick and dirty tool for letting your stream play Dropmix vs you


## Small description

[Dropmix](https://dropmix.hasbro.com/) is a music mixing card game from Harmonix that is played using a physical board and a tablet or smartphone.  Normally, both players have to be in the same physical space in order to play, but I was curious if it was possible for players to play against each other over the internet.  Furthermore, I wanted to try this out playing against someone on my Twitch stream and against the Twitch audience.  That's where this quick and dirty script was born.

## How to Use

This script is built for Python 2.  Right now, I have 5 premade decks programmed: Sweets, Highness, Blade, Controller, and Mirrors. I would have also programmed Derby, but that would have meant that I would need to write (and think of a non-terrible way for my opponent) to play Searching Within (Search your deck for a card, draw it, then shuffle your deck). 

Basically, you play your hand normally in physical space. To manage your opponent's hand, you run the program and it will ask which two playlists your opponent wants to use. Enter the first one, press enter, enter the second one and press enter again. The deck information will be written to `hand.txt`. `hand.txt` should be used as a text source in OBS (or your streaming app of choice) to show the hand. The program will shuffle your opponent's decks, draw 5 cards, write the hand information to `deck.txt` and then prompt you for an action.  The actions you can enter are:

1) `d` -- draw a card
2) `d2` -- draw 2 cards
3) any number -- play that numbered card from the hand

When your stream/opponent tells you what card to play, they should tell you something like "I want to play the vocals for Call Me Maybe. It is card number 4 in my hand, from Sweets and place it in the first slot on the board."  You will fish out that card from the sweets pack (this requires you to have the physical card on hand), and place it on the board to actually play it. Then continue. KEEP IN MIND THAT WHEN A CARD IS PLAYED, THE CARD NUMBERS MAY CHANGE! FACTOR THIS IN.

## Caveats

Like I said, this is quick and dirty.  There is no error handling nor is there any recovery if you make a mistake.  Play with it a few times before you do it for real.


-----

This project is not affiliated, operated, nor sponsored by Harmonix Music Systems, Inc. Dropmix and all related titles and logos are trademarks of Harmonix Music Systems, Inc. All Rights Reserved.
