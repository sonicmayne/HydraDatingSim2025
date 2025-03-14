#
# Code by: Revierr
# Date: 2/4/2025
# Filename: relationshipmenu.rpy
#
# This is a code asset for an easy plug in and play relationship menu for a Renpy visual novel!
#
# You may use this code for free, within any commercial or noncommercial projects, with or without credit! Thanks!
# If you credit me, please link it to my itch.io (https://revierr.itch.io/)

#YOUR TASKS ARE:
#1. Fill in the character names at line 20 and beyond
#2. Paste code starting at line 20 into script.rpy at the very top! (It works if you don't do this, but you want to make sure the game loads the variables first so it knows they exist.)
#3. Add a line in your script.rpy after the start label that says "show screen button" (If you're fancy, try "show screen button with dissolve")
#4. Have fun micromanaging your relationship points!


#Cut and paste the following code into the top of your script.rpy file. V

# default character1affection = 50 #These are where the bar starts. If you make more bars, you need more of these too!
# default character2affection = 50

# default maxpoints = 100 #This is the highest points a character can have. Think of the bars like ratios, if you start at 50 then your bar is 50/100 (or 50%) full! This line here changes the 100.

# default character1= "Character 1" #Replace the part in quotes with your character's name. If you don't see it update live, restart the game!
# default character2= "Character 2"

#Above code needs to go into script.rpy. ^

#Now, whenever you want to change the bar you change the variable character1affection.
#For example, to make the bar increase you put "$ character1affection += 10"


#This code defines the button that appears while the game is playing regularly.
screen button:
    # xalign and yalign are the positions on screen if you'd like to move it around.
    vbox xalign 0.95 yalign 0:

        imagebutton:
        #These are the visuals for the button. You can use the same image, or have it change when hovered!
        #The game looks for the button in "game/images" if you remove the "gui/"
        #Make the actual file of the button image larger if you'd like a bigger button!!!
            idle "gui/button.png"
            hover "gui/hoverbutton.png"
            action ui.callsinnewcontext("relationshipmenu")

#This chunk of code defines the range the variable needs to be within to show an emotion!
#You can add more or take some away. Please keep the numbers in descending order, like 80, 50, 20, 10.

init python:
    def emotions(points):
        if points >= 100:
            return "absolutely crazy for you"
        if points >= 80:
            return "in love with you"
        elif points >= 40:
            return "indifferent to you"
        elif points >= 30:
            return "disliking you"
        else:
            return "strongly disliking you"
#If you want different characters to have different sets of emotions, you can copy the above code starting at "init python:"
#then paste it below. Then, change the emotion ranges and names! Lastly, on the line "def emotions(points)" you need to change "emotions" to a new word,
#I suggest the character's name followed by emotions so you remember it better!

#This code defines the shape of the menu!
style relationmenustyles:
    padding (60, 60)
    background Frame("gui/affs.png") #If you rename the background picture, change this code too.
    #These following two lines center the menu! If you want it to stick to the side, you can change xalign to 0.0, or 1.0. Do whatever really.
    xalign 0.5
    yalign 0.5

#This is the data that shows inside the menu.
screen relationmenu:
    window:
        style "relationmenustyles"

        vbox:
            #This line defines the spacing between all of the "hboxes", increase it to make the bars and nametags further apart.
            spacing 20

            #Title!
            hbox:
                xalign 0.5 #Centered
                label "{b}{color=#fff}{size=+5}Relationships{/b}{/color}" #Swap out #fff for any hexcode to change the color, and size adds to the base text size of your VN so it will be bigger!!!

            hbox:
                xalign 0.5
                label " {b}{color=#fff}[characterA] is {/b}{/color}[emotions(aAffection)]" yalign 0.5#If you made a new emotion list for a character, change the word "emotions" to the new word you made.
            hbox:
                xalign 0.5
                bar range maxpoints value aAffection xmaximum 500 #xmaximum is how wide the bar can go
            hbox:
                xalign 0.5
                label " {b}{color=#fff}[characterB] is {/b}{/color}[emotions(bAffection)]" yalign 0.5
            hbox:
                xalign 0.5
                bar range maxpoints value bAffection xmaximum 500 #xmaximum is how wide the bar can go
            hbox:
                xalign 0.5
                label " {b}{color=#fff}[characterC] is {/b}{/color}[emotions(cAffection)]" yalign 0.5
            hbox:
                xalign 0.5
                bar range maxpoints value cAffection xmaximum 500 #xmaximum is how wide the bar can go
            hbox:
                xalign 0.5
                label " {b}{color=#fff}[characterD] is {/b}{/color}[emotions(dAffection)]" yalign 0.5
            hbox:
                xalign 0.5
                bar range maxpoints value dAffection xmaximum 500 #xmaximum is how wide the bar can go
            #This button closes the menu
            textbutton "Return" action Return() xalign 0.5 #You can uncenter the return button by removing "xalign 0.5"

#Simplifying the process of showing the menu, so you can just say "show screen relationmenu"
label relationshipmenu:
    call screen relationmenu
    return