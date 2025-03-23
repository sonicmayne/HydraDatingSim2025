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

init python:
    def blockProgress():
        if renpy.music.is_playing("sound"):
            renpy.pause((20-renpy.music.get_pos('sound')),hard=True)

# The game starts here.

label start:

    play music "IntroMusic.mp3"
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
            y "Thanks, I guess?"
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
                    y "It wasn't really that good..."
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

    h "You're pretty okay, I guess you can have our contact details, here's our business card"
    y "You have a business card? What for?"
    h "Read it and find out"
    y "'Many Heads Are Better Than One' - A Conflict Resolution Agency"
    h "Well, we'd better be off, we've got a conflict to resolve. See you around?"

    y "Later that night, I went home and forgot about the whole thing."
    y "The next morning, I woke up convinced it was a dream - until I found the business card in my pocket"
    y "After that, I invited the Hydra to..."

    default menuset = set()
    default datechoices = 0

    menu dates:
        set menuset
        "karaoke":
            $ datechoices += 1
            jump karaoke
        "theme park":
            $ datechoices += 1
            jump themepark
        "beach":
            $ datechoices += 1
            jump beach
        "axe throwing":
            $ datechoices += 1
            jump axe
        "art gallery":
            $ datechoices += 1
            jump art

    label karaoke:
        y "Karaoke, how about it?"
        a "What makes you think I'd like that?"
        b "I think I should choose what we - your idea sounds tedious"
        c "I'd like to go"
        d "As would I, another brilliant idea!"
        y "With that in mind, we went to the karaoke"
        show bg karaoke
        y "So, what we singing? I'll scroll through the options"
        y "Hydra is a Place on Earth?"
        # play music "heaven.mp3"
        $ blockProgress
        y "Total Eclipse of the Heads?"
        # play music "heart.mp3"
        $ blockProgress
        y "Hydra Killed the Radio Star?"
        # play music "radio.mp3"
        $ blockProgress
        y "Heads of the Hydra?"
        # play music "eye.mp3"
        $ blockProgress
        a "All of your suggestions are awful"
        b "I wholeheartedly agree, are you an idiot?"
        a "Hey, let's do this one!"
        # play music "friday night.mp3"
        $ blockProgress
        c "Wow, you're great at karaoke!"
        a "I'm ashamed to admit it, but you do have a rather good voice"
        $ aAffection += 10
        $ cAffection += 10
        y "You guys are too kind, I think you'd have a much better singing voice than I do"
        a "Well, you're not finding out. We're off."
        jump reshowdates

    label themepark:
        y "What about Yeetland?"
        a "That could be okay, I guess..."
        b "No, it's an awful idea. As was expected of you."
        c "What are we waiting for!? Let's go, posthaste!"
        d "I have a fear of heights, but let's do it!"
        show bg themepark
        d "Let's go on the Tea Cups!"
        d "Wait, let's do the Dodgems first!"
        d "Wait, wait, let's do the maze!"
        b "Those suggestions are pretty bland, I say we go on the Pirate Ship!"
        d "But I don't like heights..."
        b "Then how about the Twister or the Chair Planes then?"
        d "Those do sound better..."
        b "Don't tell me you don't like fast rides too?!"
        d "I plead the fifth!"
        y "Hey, no need to get so argumentative over it - we can do them all, and you can close you're eyes if you're scared. Sound good?"
        a "Where's my say?"
        c "I want to try everything!"
        y "..."
        y "We went on all the rides, and I'm exhausted, everything feels like its moving"
        d "Thank you for making me go past my boundaries..."
        b "Not only should you thank us, you should be praising us!"
        y "Calm down..."
        y "Hey, before we go, want to go on the Cola Colossus?"
        d "We are not going on a rollercoaster"
        y "Why not? I thought you had great fun on the rides"
        d "I did, but that's crossing a line"
        a "I don't like rollercoasters so I vote against it"
        b "Me too"
        c "I must admit, I do wish to, but I know when I'm outvoted"
        y "Ah well, it was just an idea..."
        y "Are you thirsty?"
        a "Yes, I'll have a water."
        b "Water."
        c "Please may I have a chocolate milkshake?"
        d "Can I have a watermelon soda please?"
        y "Coming right up!"
        y "..."
        y "Here you all go. I rather do hope you enjoy, especially at these prices"
        a "You should be grateful for the opportunity to serve me"
        y "Hmm... I do wonder about that..."
        a "Thank you for today"
        b "Yeah, it was nice..."
        c "YOU'RE THE BEST"
        d "YOU REALLY ARE"
        y "Thanks - I had fun too"
        jump reshowdates

    label beach:
        y "Beach?"
        a "Water waste of time"
        b "The only beach here is you"
        c "Sounds good to me"
        d "Me too! Me too!"
        show bg beach
        play music "Despacito.mp3"
        y "The waves were gently lapping against the shore, with foam rolling onto the sand, and the seabirds were lulling around on the sand."
        a "Why are you narrating this like it's a documentary?"
        y "Wait? I said that out loud?!"
        a "Either that or I can read your mind you fool"
        y "Heh"
        c "Let's get ice cream!"
        d "No, lets' get a watermelon!"
        a "We're getting ice cream, and that's that. Well, you're getting the ice cream"
        y "Ice cream sounds delightful on a great day like today. What do you all want?"
        a "Mint"
        b "Chocolate"
        c "Bubblegum"
        d "Watermelon"
        y "Is watermelon a flavour of ice cream?"
        d "Not sure, I want watermelon though"
        y "Well, I'll do my best."
        y "..."
        if dAffection > 0:
            y "Right, I'm back, I was able to get you a watermelon too!"
            $ dAffection += 5
            d "Wow - you're actually incredible."
        else:
            y "Right, I'm back. I was unable to get you a watermelon, sorry. I did get you some strawberry ice cream, so I hope that you like that!"
            d "Thank you - I'm sure it'll be fine"
        a "Thank you for the ice cream"
        b "Yeah, thanks, I guess..."
        c "THANK YOU"
        y "No need to shout - I'm just glad you're enjoying it"
        y "..."
        y "Huh, wanna go for a dip in the sea?"
        a "I like the cut of your jib"
        y "What?"
        a "Err, nothing, ignore that! Yes, I would like to go"
        b "Well, I certainly don't!"
        a "Well, I do!"
        b "Well, I certainly don't!"
        a "Well, I do!"
        b "Well, I certainly don't!"
        a "Well, I do!"
        b "Well, I certainly don't!"
        a "Well, I do!"
        b "Well, I certainly don't!"
        a "Well, I do!"
        y "Uh, guys? Wanna stop the arguing?"
        a "I WANT TO SWIM"
        b "I DON'T"
        c "Hey, let's vote on it - I would like the swimming very much"
        d "Me too"
        b "I can't argue with democracy"
        y "*splash*"
        y "Hey, stop splashing the water in my face!"
        b "I don't know why I didn't want to do this - this is great fun"
        c "I'm having fun in the sun"
        y "*splash splash*"
        y "..."
        y "Well, I'm beat, see you tomorrow?"
        h "Sure!"
        $ aAffection += 5
        $ bAffection += 5
        $ cAffection += 5
        $ dAffection += 5
        jump reshowdates

    label axe:
        y "Axe throwing?"
        a "No!"
        b "No!"
        c "No!"
        d "No!"
        y "It was just a suggestion!"
        a "Well, you can take your suggestion and move it where the sun doesn't shine"
        y "Who knew it was so easy to wind up a Hydra"
        a "Choose your next actions very wisely"
        menu:
            "Double down":
                y "You know you want to..."
                a "Right, that's it."
                b "Can I unleash my full fury?"
                a "Yes"
                y "..."
                y "I am slowly losing my grip on reality"
                y "I probably shouldn't do that again"
                return
            "Concede the point":
                y "All right let's do something else"
                jump reshowdates

    label art:
        y "Art gallery?"
        show bg gallery
        jump reshowdates

    label reshowdates:
        if datechoices <= 2:
            jump dates


    # This ends the game.

    return
