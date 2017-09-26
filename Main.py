#!/usr/bin/env python

from database.Decks import get_decks
import random

STREAM_HAND = []
STREAM_DECK = []

DECKS = get_decks()


def write_hand_list():
    with open('hand.txt', 'w') as f:
        lines = ["Twitch's Hand:\n", "\n"]
        for x in range(len(STREAM_HAND)):
            lines.append("%d) %s\n" % (x + 1, STREAM_HAND[x]))
        f.writelines(lines)
        f.close()


def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def main_loop():
    while True:
        write_hand_list()
        print "What does the stream do?"
        print "number = play that card"
        print "d = draw 1 card"
        print "d2 = draw 2 cards"

        choice = raw_input()

        if choice == "d":
            print "Drew 1"
            draw_card(1)
        elif choice == "d2":
            print "Drew 2"
            draw_card(2)
        elif is_int(choice):
            if int(choice) <= len(STREAM_HAND):
                print "Played card"
                card_num = int(choice)
                del STREAM_HAND[card_num - 1]


def draw_card(count):
    for x in range(count):
        card = STREAM_DECK.pop()
        STREAM_HAND.append(card)


if __name__ == '__main__':
    print "Initializing"

    print "Available decks: "
    for (k, v) in DECKS.iteritems():
        print "\t %s" % k

    print "Which decks would you like to play with?"
    deck1 = raw_input().upper()
    deck2 = raw_input().upper()

    STREAM_DECK = DECKS[deck1] + DECKS[deck2]
    random.shuffle(STREAM_DECK)

    print "Made deck of %d cards" % len(STREAM_DECK)

    print "Drawing 5 cards"
    draw_card(5)

    main_loop()
