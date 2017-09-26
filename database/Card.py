class Card:
    def __init__(self, artist, title, level, color, instrument, deck):
        self.artist = artist
        self.title = title
        self.level = level
        self.color = color
        self.instrument = instrument
        self.deck = deck

    def __repr__(self):
        return "%s - Level %d - %s - %s - %s (%s)" % (self.color, self.level, self.instrument, self.artist, self.title, self.deck)

