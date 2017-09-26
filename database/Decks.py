from Card import Card


def get_decks():
    return {
        'SWEETS':
            [Card("Bruno Mars", "24k Magic", 2, "Wild", "V/K/D/K", "S"),
             Card("Carly Rae Jepsen", "Call Me Maybe", 2, "Yellow", "Vocals", "S"),
             Card("Sia", "Chandelier", 3, "Yellow", "Vocals", "S"),
             Card("Ricky Martin", "La Mordidita (Ft. Youtel)", 1, "Red", "Horns", "S"),
             Card("The Lingala Sound", "Crystal Beach", 1, "Red", "Keys", "S"),
             Card("Sia", "Chandelier", 2, "Red", "Keys", "S"),
             Card("Megan Trainor", "All About That Bass", 3, "Red", "Guitar", "S"),
             Card("Freda Turner", "Hard Light", 1, "Blue", "Drums", "S"),
             Card("The Lingala Sound", "Crystal Beach", 1, "Blue", "Drums", "S"),
             Card("CHVRCHES", "The Mother We Share", 2, "Blue", "Drums", "S"),
             Card("Ricky Martin", "La Mordidita (Ft. Youtel)", 3, "Blue", "Drums", "S"),
             Card("Sam Hunt", "House Party", 2, "Green", "Guitar", "S"),
             Card("Carly Rae Jepsen", "Call Me Maybe", 3, "Green", "Strings", "S"),
             Card("Lift Your Voice", "(Play an Extra Vocals Card)", 2, "White", "FX", "S"),
             Card("Clear Your Mind", "(Clear 1 Random Opponent Card)", 2, "White", "FX", "S")],
        'HIGHNESS':
            [Card("Childish Gambino", "Heartbeat", 2, "Wild", "V/K/D/K", "H"),
             Card("The Weeknd", "Can't Feel My Face", 2, "Yellow", "Vocals", "H"),
             Card("A Tribe Called Quest", "Scenario", 3, "Yellow", "Vocals", "H"),
             Card("Charm Syndicate", "All Frazzled", 1, "Red", "Horns", "H"),
             Card("Sean Paul", "Temperature", 1, "Red", "Keys", "H"),
             Card("Run DMC", "It's Tricky", 2, "Red", "Guitar", "H"),
             Card("Flo Rida", "I Don't Like It, I Love It", 3, "Red", "Guitar", "H"),
             Card("Bullwheel", "Atomic Handbrake", 1, "Blue", "Drums", "H"),
             Card("Charm Syndicate", "All Frazzled", 1, "Blue", "Drums", "H"),
             Card("Far East Movement", "Like a G6", 2, "Blue", "Drums", "H"),
             Card("Run DMC", "It's Tricky", 3, "Blue", "Drums", "H"),
             Card("A Tribe Called Quest", "Scenario", 2, "Green", "Guitar", "H"),
             Card("The Weeknd", "Can't Feel My Face", 3, "Green", "Guitar", "H"),
             Card("Flame Out", "(+1 Point for Each Blue Card)", 2, "White", "FX", "H"),
             Card("Roll Up", "(Draw 1 Card)", 3, "White", "FX", "H")],
        'BLADE':
            [Card("Disturbed", "Down With The Sickness", 2, "Wild", "V/G/D/G", "B"),
             Card("Evanescence", "Bring Me To Life", 2, "Yellow", "Vocals", "B"),
             Card("Ed Sheeran", "Sing", 3, "Yellow", "Vocals", "B"),
             Card("Ed Sheeran", "Sing", 1, "Red", "Guitar", "B"),
             Card("Warlords of the Old West", "Strychnine Baby", 1, "Red", "Guitar", "B"),
             Card("Cake", "Short Skirt/Long Jacket", 2, "Red", "Horns", "B"),
             Card("Weezer", "King of the World", 3, "Red", "Guitar", "B"),
             Card("Pinhole Cage", "Just About to Snap", 1, "Blue", "Drums", "B"),
             Card("Warlords of the Old West", "Strychnine Baby", 1, "Blue", "Drums", "B"),
             Card("Cake", "Short Skirt/Long Jacket", 2, "Blue", "Drums", "B"),
             Card("Imagine Dragons", "Radioactive", 3, "Blue", "Drums", "B"),
             Card("Fall Out Boy", "Centuries", 2, "Green", "Guitar", "B"),
             Card("Evanescence", "Bring Me to Live", 3, "Green", "Guitar", "B"),
             Card("Strings of Fate", "(Play an extra Guitar card)", 2, "White", "FX", "B"),
             Card("The Heartless One", "(Clear all Opponent blue cards)", 2, "White", "FX", "B")],
        'CONTROLLER':
            [Card("Skrillex", "Bangarang", 2, "Wild", "V/G/D/K", "C"),
             Card("The Chainsmokers", "Closer", 2, "Yellow", "Vocals", "C"),
             Card("Jason Derulo", "Want to Want Me", 3, "Yellow", "Vocals", "C"),
             Card("James Landino", "Break for Me", 1, "Red", "Keys", "C"),
             Card("The Chainsmokers", "Closer", 1, "Red", "Guitar", "C"),
             Card("ODESZA", "Say My Name", 2, "Red", "Keys", "C"),
             Card("Afrojack", "Take Over Control", 3, "Red", "Keys", "C"),
             Card("Billzantium", "Wishin' I Had It Now", 1, "Blue", "Drums", "C"),
             Card("James Landino", "Break for Me", 1, "Blue", "Drums", "C"),
             Card("Afrojack", "Take Over Control", 2, "Blue", "Drums", "C"),
             Card("Duck Sauce", "Barbara Steisand", 3, "Blue", "Drums", "C"),
             Card("Jason Derulo", "Want to Want Me", 2, "Green", "Guitar", "C"),
             Card("LMFAO", "Sexy and I Know It", 3, "Green", "Guitar", "C"),
             Card("Assert Order", "(+2 points for owning a green card)", 2, "White", "FX", "C"),
             Card("Embrace Chaos", "(-2 points from opponent)", 2, "White", "FX", "C")],
        'MIRRORS':
            [Card("Ginuwine", "Pony", 2, "Wild", "V/K/D/V", "M"),
             Card("Sant-N-Pepa", "Push It", 2, "Yellow", "Vocals", "M"),
             Card("Outkast", "Ms. Jackson", 3, "Yellow", "Vocals", "M"),
             Card("Bignums", "Larry's Place (Part II)", 1, "Red", "Sampler", "M"),
             Card("Bullwheel", "Atomic Handbrake", 1, "Red", "Keys", "M"),
             Card("Dillzan Madan", "Main Mistar Praim Hoon", 2, "Red", "Guitar", "M"),
             Card("Salt-N-Pepa", "Push It", 3, "Red", "Keys", "M"),
             Card("Sean Paul", "Temperature", 1, "Blue", "Drums", "M"),
             Card("The Weeknd", "Can't Feel My Face", 1, "Blue", "Drums", "M"),
             Card("Dillzan Madan", "Main Mistar Praim Hoon", 2, "Blue", "Drums", "M"),
             Card("A Tribe Called Quest", "Scenario", 3, "Blue", "Drums", "M"),
             Card("Bullwheel", "Atomic Handbrake", 2, "Green", "Horns", "M"),
             Card("Outkast", "Ms. Jackson", 3, "Green", "Guitar", "M"),
             Card("Lay It Down", "Play an Extra Red Card", 2, "White", "FX", "M"),
             Card("Bust It Up", "+2 Points for each Drums/Vocals Pair", 2, "White", "FX", "M")
             ]
    }