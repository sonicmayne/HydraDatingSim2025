# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("") # Narrator has no name
define h = Character("Hydra")
define a = Character("Phoebe")
define b = Character("Alice")
define c = Character("Rhea")
define d = Character("Theia")

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
            y "I'm sorry, I;ll be on my way now"
        "Soda":
            b "I think you'll find that's mine."
            y "She look my soda. I'm still dehydra-ted, but somehow, I think I'll be fine."
            b "Wait, this isn't Diet, what are you tryng to do to me?!"
            y "It wasn't intended for you in the first place"
            b "Here, you can have it back"
            y "Thanks, I guess?"
        "Limeade":
            c "Awww, that was the last limeade. Don't worry about me, go and enjoy it. I'll stay here and think about other options..."
            y "You can have it if you really want it"
            c "No, go ahead and enjoy yourself whilst I remain like limeade itself, sour"
        "Beer":
            h "Hmph, such an unsophisticed drink, suits an unsophisticated person."
            y "I sometimes think back to that date and wonder what could have been"
            return
        "Wine":
            d "Wine?! TRuly the drinks of the gods! One does appreciate how it tastes. You've really made the right call here!"
        # Possibly better to set variables incrementing the relationship with each head.
        # TODO store choices

    # This ends the game.

    return
