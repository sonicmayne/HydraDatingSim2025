# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("") # Narrator has no name
define h = Character("Hydra") # The Hydra as a whole
define a = Character("Phoebe")
define b = Character("Alice")
define c = Character("Rhea")
define d = Character("Theia")

default aAffection = 0
default bAffection = 0
default cAffection = 0
default dAffection = 0

default maxpoints = 100 #This is the highest points a character can have.

default characterA = "Phoebe"
default characterB = "Alice"
default characterC = "Rhea"
default characterD = "Theia"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    show screen button with dissolve

    # These display lines of dialogue.

    y "It started when I was needing hydra-ted. The Hydra was there, with each head arguing amongst themselves, whilst perusing the drinks aisle, arguing about which brand of drink to buy."
    y "Then, all the heads turned to me and proceeded to stare at me, so I decided to pick up some..."

    default headA = 0
    default headB = 0
    default headC = 0
    default headD = 0
    menu:
        "Water":
            a "Water? Suits a plain fool, such as yourself."
            y "THanks, I guess?"
            a "You dare talk back to me? Who do you think you are?"
            y "I'm sorry, I'll be on my way now..."
            a "Please, don't go..."
            $ aAffection += 5
        "Soda":
            b "I think you'll find that's mine."
            y "She look my soda. I'm still dehydra-ted, but somehow, I think I'll be fine."
            b "Wait, this isn't Diet, what are you tryng to do to me?!"
            y "It wasn't intended for you in the first place!"
            b "Here, you can have it back"
            y "Thanks, I guess?"
            $ bAffection += 5
        "Limeade":
            c "Awww, that was the last limeade. Don't worry about me, go and enjoy it. I'll think about other options..."
            y "You can have it if you really want it..."
            c "No, go ahead and enjoy yourself whilst I remain like limeade itself, sour"
            y "Here, I'll take the water "
            $ cAffection += 5
        "Beer":
            h "Hmph, such an unsophisticed drink, suits an unsophisticated person."
            y "The Hydra look really perturbed, then left, muttering that beer was a layman's drink"
            y "I sometimes think back to that day and wonder what could have been"
            return
        "Wine":
            d "Wine?! Truly the drinks of the gods! One does appreciate how it tastes. You've really made the right call here!"
            y "It's only wine, but I must concur with you if I'm honest"
            d "See?! I knew you'd get it."
            $ dAffection += 5

    menu:
        "Suddenly I felt the urge to.."
        "Use a pickup line":
            menu:
                "Damn, if I knew this was a date, I'd have dressed up":
                    b "Looking at the way you're dressed, I'd have thought it was a reunion of Adam West's Batman and Robin"
                    y "I'm like Batman? That's ace!"
                    b "No, you're Robin"
                    y "Ouch"
                    $ bAffection += 5
                "Even if there was no gravity, I'd still fall for you":
                    a "The cheek to talk to me like that!"
                    a "Well, thanks for the compliment I guess"
                    $ aAffection += 5
        "Tell a joke":
            menu:
                "I had a hydra joke, but it got ahead of itself":
                    c "*hee hee*"
                    $ cAffection += 5
                "Some people are hydrophobic, I'm hydraphobic":
                    d "Wow, that's clever, like so clever! How do you manage it?"
                    $ dAffection += 5
        "Shout 'FIRE!'":
            h "WHAT?! WHERE?!"
            y "The Hydra frantically looked around for the source of the fire, before realising I was playing a prank"
            h  "YOU DARE FIND THIS FUNNY?"
            y "Sure do!"
            y "The next thing I knew, one of the heads fired something that looked like a capsule right at me, but I ducked out of the way"
            y "Whoa! A little uncalled for, don't you think?!"
            h "No - you deserve the full might of my range!"
            y "Another shot flew out, but once again, I dodged out of the way"
            y "Is that all you've got?"
            y "The next thing I knew, I woke up in hospital. I don't know what happened to the Hydra after that"
            return

    h "Here's our phone number."

    y "After that, I invited the Hydra to..."
    menu:
        "karaoke":
            y "Placeholder"
        "the theme park":
            y "Placeholder"

    # This ends the game.

    return
