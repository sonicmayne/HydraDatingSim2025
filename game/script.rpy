# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("") # Narrator has no name
define h = Character("Hydra") # The Hydra as a whole
define a = Character("Phoebe")
define b = Character("Alice")
define c = Character("Rhea")
define d = Character("Theia")

image black = "#000"

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
        if renpy.music.is_playing('sound'):
            remaining_duration = 22
            renpy.pause(remaining_duration, hard=True)
            
transform t:
    zoom 0.5
    xpos 0.4
    ypos 0.25

# The game starts here.

label start:

    play music "IntroMusic.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    y "It started when I was needing hydra-ted. The Hydra was there, with each head arguing amongst themselves, whilst perusing the drinks aisle, arguing about which brand of drink to buy."
    y "Then, all the heads turned to me and proceeded to stare at me, so I decided to pick up some..."
    show hydra at t

    default headA = 0
    default headB = 0
    default headC = 0
    default headD = 0
    menu:
        "Water":
            hide hydra with dissolve
            show a at t
            a "Water? Suits a plain fool, such as yourself."
            y "Thanks, I guess?"
            a "You dare talk back to me? Who do you think you are?"
            y "I'm sorry, I'll be on my way now..."
            a "Please, don't go..."
            $ aAffection += 5
        "Soda":
            hide hydra with dissolve
            show b at t
            b "I think you'll find that's mine."
            y "She look my soda. I'm still dehydra-ted, but somehow, I think I'll be fine."
            b "Wait, this isn't Diet, what are you tryng to do to me?!"
            y "It wasn't intended for you in the first place!"
            b "Here, you can have it back"
            y "Thanks, I guess?"
            $ bAffection += 5
        "Limeade":
            hide hydra with dissolve
            show c at t
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
            hide hydra with dissolve
            show d at t
            d "Wine?! Truly the drinks of the gods! One does appreciate how it tastes. You've really made the right call here!"
            y "It's only wine, but I must concur with you if I'm honest"
            d "See?! I knew you'd get it."
            $ dAffection += 5
            
    hide a with dissolve
    hide b with dissolve
    hide c with dissolve
    hide d with dissolve
    hide hydra with dissolve

    menu:
        "Suddenly I felt the urge to.."
        "Use a pickup line":
            menu:
                "Damn, if I knew this was a date, I'd have dressed up":
                    show b at t
                    b "Looking at the way you're dressed, I'd have thought it was a reunion of Adam West's Batman and Robin"
                    y "I'm like Batman? That's ace!"
                    b "No, you're Robin"
                    y "Ouch"
                    $ bAffection += 5
                "Even if there was no gravity, I'd still fall for you":
                    show a at t
                    a "The cheek to talk to me like that!"
                    a "Well, thanks for the compliment I guess"
                    $ aAffection += 5
        "Tell a joke":
            menu:
                "I had a hydra joke, but it got ahead of itself":
                    show c at t
                    c "*hee hee*"
                    $ cAffection += 5
                "Some people are hydrophobic, I'm hydraphobic":
                    show d at t
                    d "Wow, that's clever, like so clever! How do you manage it?"
                    y "It wasn't really that good..."
                    $ dAffection += 5
        "Shout 'FIRE!'":
            show h at t
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

    hide a with dissolve
    hide b with dissolve
    hide c with dissolve
    hide d with dissolve
    hide hydra with dissolve
    
    show hydra at t
    
    h "You're pretty okay, I guess you can have our contact details, here's our business card"
    y "You have a business card? What for?"
    h "Read it and find out"
    y "'Many Heads Are Better Than One' - A Conflict Resolution Agency"
    h "Well, we'd better be off, we've got a conflict to resolve. See you around?"
    hide hydra with dissolve
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
        show a at t
        a "What makes you think I'd like that?"
        hide a with dissolve
        show b at t
        b "I think I should choose what we - your idea sounds tedious"
        hide b with dissolve
        show c at t
        c "I'd like to go"
        hide c with dissolve
        show d at t
        d "As would I, another brilliant idea!"
        hide d with dissolve
        y "With that in mind, we went to the karaoke"
        stop music
        show bg karaoke
        y "So, what we singing? I'll scroll through the options"
        play sound "heaven.mp3"
        y "Hydra is a Place on Earth?"
        $ blockProgress()
        play sound "heart.mp3"
        y "Total Eclipse of the Heads?"
        $ blockProgress()
        play sound "mind.mp3"
        y "Always on My Head?"
        $ blockProgress()
        play sound "eye.mp3"
        y "Heads of the Hydra?"
        $ blockProgress()
        show a at t
        a "All of your suggestions are awful"
        hide a with dissolve
        show b at t
        b "I wholeheartedly agree, are you an idiot?"
        hide b with dissolve
        a "Hey, let's do this one!"
        # play music "friday night.mp3"
        $ blockProgress()
        show c at t
        c "Wow, you're great at karaoke!"
        hide c with dissolve
        show a at t
        a "I'm ashamed to admit it, but you do have a rather good voice"
        $ aAffection += 10
        $ cAffection += 10
        y "You guys are too kind, I think you'd have a much better singing voice than I do"
        a "Well, you're not finding out. We're off."
        hide a with dissolve
        jump reshowdates

    label themepark:
        y "What about Yeetland?"
        show a at t
        a "That could be okay, I guess..."
        hide a with dissolve
        show b at t
        b "No, it's an awful idea. As was expected of you."
        hide b with dissolve
        show c at t
        c "What are we waiting for!? Let's go, posthaste!"
        hide c with dissolve
        show d at t
        d "I have a fear of heights, but let's do it!"
        show bg themepark
        d "Let's go on the Tea Cups!"
        d "Wait, let's do the Dodgems first!"
        d "Wait, wait, let's do the maze!"
        hide d with dissolve
        show b at t
        b "Those suggestions are pretty bland, I say we go on the Pirate Ship!"
        hide b with dissolve
        show d at t
        d "But I don't like heights..."
        hide d with dissolve
        show b at t
        b "Then how about the Twister or the Chair Planes then?"
        hide b with dissolve
        show d at t
        d "Those do sound better..."
        hide d with dissolve
        show b at t
        b "Don't tell me you don't like fast rides too?!"
        hide b with dissolve
        show d at t
        d "I plead the fifth!"
        hide d with dissolve
        y "Hey, no need to get so argumentative over it - we can do them all, and you can close you're eyes if you're scared. Sound good?"
        show a at t
        a "Where's my say?"
        hide a with dissolve
        show c at t
        c "I want to try everything!"
        hide c with dissolve
        y "..."
        y "We went on all the rides, and I'm exhausted, everything feels like its moving"
        show d at t
        d "Thank you for making me go past my boundaries..."
        hide d with dissolve
        show b at t
        b "Not only should you thank us, you should be praising us!"
        hide b with dissolve
        y "Calm down..."
        y "Hey, before we go, want to go on the Cola Colossus?"
        show d at t
        d "We are not going on a rollercoaster"
        y "Why not? I thought you had great fun on the rides"
        d "I did, but that's crossing a line"
        hide d with dissolve
        show a at t
        a "I don't like rollercoasters so I vote against it"
        hide a with dissolve
        show b at t
        b "Me too"
        hide b with dissolve
        show c at t
        c "I must admit, I do wish to, but I know when I'm outvoted"
        hide c with dissolve
        y "Ah well, it was just an idea..."
        y "Are you thirsty?"
        show a at t
        a "Yes, I'll have a water."
        hide a wth dissolve
        show b at t
        b "Water."
        hide b with dissolve
        show c at t
        c "Please may I have a chocolate milkshake?"
        hide c with dissolve
        show d at t
        d "Can I have a watermelon soda please?"
        hide d with dissolve
        y "Coming right up!"
        y "..."
        y "Here you all go. I rather do hope you enjoy, especially at these prices"
        show a at t
        a "You should be grateful for the opportunity to serve me"
        y "Hmm... I do wonder about that..."
        a "Thank you for today"
        hide a with dissolve
        show b at t
        b "Yeah, it was nice..."
        hide b with dissolve
        show c at t
        c "YOU'RE THE BEST"
        hide c with dissolve
        show d at t
        d "YOU REALLY ARE"
        hide d with dissolve
        y "Thanks - I had fun too"
        jump reshowdates

    label beach:
        y "Beach?"
        show a at t
        a "Water waste of time"
        hide a with dissolve
        show b at t
        b "The only beach here is you"
        hide b with dissolve
        show c at t
        c "Sounds good to me"
        hide c with dissolve
        show d at t
        d "Me too! Me too!"
        hide d with dissolve
        show bg beach
        play music "Despacito.mp3"
        y "The waves were gently lapping against the shore, with foam rolling onto the sand, and the seabirds were lulling around on the sand."
        show a at t
        a "Why are you narrating this like it's a documentary?"
        y "Wait? I said that out loud?!"
        a "Either that or I can read your mind you fool"
        y "Heh"
        hide a with dissolve
        show c at t
        c "Let's get ice cream!"
        hide c with dissolve
        show d at t
        d "No, lets' get a watermelon!"
        hide d with dissolve
        show a at t
        a "We're getting ice cream, and that's that. Well, you're getting the ice cream"
        y "Ice cream sounds delightful on a great day like today. What do you all want?"
        a "Mint"
        hide a with dissolve
        show b at t
        b "Chocolate"
        hide b with dissolve
        show c at t
        c "Bubblegum"
        hide c with dissolve
        show d at t
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
        hide d with dissolve
        show a at t
        a "Thank you for the ice cream"
        hide a with dissolve
        show b at t
        b "Yeah, thanks, I guess..."
        hide b with dissolve
        c "THANK YOU"
        hide c with dissolve
        y "No need to shout - I'm just glad you're enjoying it"
        y "..."
        y "Huh, wanna go for a dip in the sea?"
        show a at t
        a "I like the cut of your jib"
        hide a with dissolve
        y "What?"
        show a at t
        a "Err, nothing, ignore that! Yes, I would like to go"
        hide a with dissolve

        show b at t
        b "Well, I certainly don't!"
        hide b with dissolve
        show a at t
        a "Well, I do!"
        hide a with dissolve

        show b at t
        b "Well, I certainly don't!"
        hide b with dissolve
        show a at t
        a "Well, I do!"
        hide a with dissolve

        show b at t
        b "Well, I certainly don't!"
        hide b with dissolve
        show a at t
        a "Well, I do!"
        hide a with dissolve

        show b at t
        b "Well, I certainly don't!"
        hide b with dissolve
        show a at t
        a "Well, I do!"
        hide a with dissolve

        show b at t
        b "Well, I certainly don't!"
        hide b with dissolve
        show a at t
        a "Well, I do!"
        hide a with dissolve

        y "Uh, guys? Wanna stop the arguing?"
        show a at t
        a "I WANT TO SWIM"
        hide a with dissolve
        show b at t
        b "I DON'T"
        hide b with dissolve
        show c at t
        c "Hey, let's vote on it - I would like the swimming very much"
        hide c with dissolve
        show d at t
        d "Me too"
        hide d with dissolve
        show b at t
        b "I can't argue with democracy"
        y "*splash*"
        y "Hey, stop splashing the water in my face!"
        b "I don't know why I didn't want to do this - this is great fun"
        hide b with dissolve
        show c at t
        c "I'm having fun in the sun"
        hide c with dissolve
        y "*splash splash*"
        y "..."
        y "Well, I'm beat, see you tomorrow?"
        show hydra at t
        h "Sure!"
        hide hydra with dissolve
        $ aAffection += 5
        $ bAffection += 5
        $ cAffection += 5
        $ dAffection += 5
        jump reshowdates

    label axe:
        y "Axe throwing?"
        show a at t
        a "No!"
        hide a with dissolve
        show b at t
        b "No!"
        hide b with dissolve
        show c at t
        c "No!"
        hide c with dissolve
        show d at t
        d "No!"
        hide d with dissolve
        y "It was just a suggestion!"
        show a at t
        a "Well, you can take your suggestion and move it where the sun doesn't shine"
        y "Who knew it was so easy to wind up a Hydra"
        a "Choose your next actions very wisely"
        menu:
            "Double down":
                y "You know you want to..."
                a "Right, that's it."
                hide a with dissolve
                show b at t
                b "Can I unleash my full fury?"
                hide b with dissolve
                show a at t
                a "Yes"
                y "..."
                y "I am slowly losing my grip on reality"
                y "I probably shouldn't do that again"
                return
            "Concede the point":
                y "All right let's do something else"
                hide a with dissolve
                jump reshowdates

    label art:
        y "Art gallery?"
        show a at t
        a "Yeah, let's do that"
        hide a with dissolve
        show b at t
        b "I'm surprised you'd suggest something so cultured"
        hide b with dissolve
        show c at t
        c "I'm not an art fan, but I'd.. like that"
        hide c with dissolve
        show d at t
        d "Let's go!"
        hide d with dissolve
        show bg gallery
        show a at t
        a "Wow, the artwork here is pretty good!"
        y "That's a mirror..."
        a "Exactly!"
        hide a with dissolve
        show b at t
        b "I dunno, this background looks pretty generic to me"
        hide b with dissolve
        show c at t
        c "It's fine - what matters is the writing right?"
        hide c with dissolve
        show b at t
        b "I guess - it's not very good is it?"
        hide b with dissolve
        show d at t
        d "I like it"
        hide d with dissolve
        y "What are you on about?"
        show a at t
        a "I'd ignore it if I were you"
        y "Okay..."
        a "This art gallery is nice - there's not much artwork in it, but the stuff that's here is amazing"
        hide a with dissolve
        show b at t
        b "I don't like this one..."
        hide b with dissolve
        show d at t
        d "What is it?"
        hide d with dissolve
        show b at t
        b "It's a depicion of a Hydra being killed by Hercules"
        hide b with dissolve
        show a at t
        a "Well, that's canonically not true, people can make their own stories"
        y "Uhh, what is the canonically true story"
        a "Well..."
        y "...2 hours later..."
        a "... and that's why it's not true!"
        y "That explains so much!"
        a "I'm tired, let's go!"
        hide a with dissolve
        jump reshowdates

    label reshowdates:
        if datechoices <= 2:
            jump dates

    hide a with dissolve
    hide b with dissolve
    hide c with dissolve
    hide d with dissolve
    hide hydra with dissolve
    scene black
    y "*BANG*"
    y "What.. was that noise?!"
    y "Why do I feel so groggy?"
    y "Mum, I don't want to go to school today..."
    y "I tried opening my eyes..."
    y "...just a bit more..."
    y "...it can't be done..."
    y "Argh!"
    scene bg room
    y "It started when I was needing hydra-ted..."
    y "Man, I need to get myself a partner if I'm getting that desparate"
    y "..."
    y "..."
    y "..."
    y "Maybe this is the dream?"

    return
