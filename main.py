#Final Project: "Ascent"

#Imports
from tkinter import *
import numpy as np
from math import *
from time import *
from random import *

#Tkinter Variables
root = Tk()
s = Canvas(root, width=875, height=572, background="#101129")


#Initializing Statistics
def setInitialStats(
):  #separate from other values as they are only reset when starting a new game
    global health, floorLvl
    health = 3
    floorLvl = -3


#Initializing Values
def setInitialValues():
    global xHealth, yHealth, xChar, yChar, xCrack, yCrack, xWeb, yWeb, xCrate, yCrate, xFinalTile, yFinalTile, click, breakCue, exiting, escDoorHeight, escDoorWidth

    global endScreenHealth, numOfCracks, numOfWebs, numOfCrates

    global xSpeed, ySpeed, charSpeed, xCrackPos, yCrackPos, xWebPos, yWebPos, xCratePos, yCratePos, cratePosX, cratePosY, xHealthPos, xEndScreenHealth, yEndScreenHealth, xEscDoor, yEscDoor, escDoorPos, xEndScreenHealthPos, nextTileX, nextTileY

    global crackDraw, charDraw, healthDraw, webDraw, crateDraw, excMarkDraw, gameOvDraw, escDoorDraw, winDraw, endScreenHealthDraw, fadeDraw, levelNumDraw, levelsBelowDraw

    global charImages, heartImage, crackImage, webImage, crateImage, excMarkImage, gameOvImages, gameLogoImage, levelsBelowImage

    global xMouse, yMouse, minX, minY, maxX, maxY, tilePosX, tilePosY, escDoorPosX, escDoorPosY, escPos, distFromDoor, lightFromDoor, typeOfTile, chanceOfBroken

    global boardCols, col, charImageIndex, fallenCase, ascendBool, gameRun, prevClick, wayOfMovement, bitMaxes, charAscend, levelNums

    global playImage, controlsImage, gameControlsImage, gameLoreInstImage, loreImage, playAgainImage, menuImage, quitImage, escapeFuncImage

    global controlButton, playButton, loreButton, menuButton, playAgainButton, quitButton

    click = False
    breakCue = False
    fallenCase = False
    gameRun = True
    ascendBool = False
    prevClick = False
    exiting = False
    charAscend = False

    xEndScreenHealth = 367
    yEndScreenHealth = 335
    endScreenHealth = 3

    xChar = 435
    yChar = 285
    xCrack = 0
    yCrack = 0
    xWeb = 0
    yWeb = 0
    xCrate = 0
    yCrate = 0

    nextTileX = 0
    nextTileY = 0

    chanceOfBroken = 0
    wayOfMovement = 0

    xCrackPos = []
    yCrackPos = []
    xHealthPos = []
    xEndScreenHealthPos = []
    xWebPos = []
    yWebPos = []
    xCratePos = []
    yCratePos = []

    typeOfTile = []
    numOfCracks = 9
    numOfWebs = 9
    numOfCrates = 18

    tilePosX = [60, 135, 210, 285, 360, 435, 510, 585, 660, 735, 810]
    tilePosY = [60, 135, 210, 285, 360, 435, 510]
    cratePosX = [135, 210, 285, 360, 435, 510, 585, 660, 735]
    cratePosY = [135, 210, 285, 360, 435]

    xFinalTile = 0
    yFinalTile = 0
    xSpeed = 0
    ySpeed = 0
    charSpeed = 0
    xMouse = 400
    yMouse = 300
    xHealth = 50
    yHealth = 50
    charDraw = 0
    crackDraw = 0
    crateDraw = 0
    gameOvDraw = 0

    levelsBelowDraw = 0
    charImageIndex = 0
    levelNumDraw = 0
    winDraw = 0
    webDraw = 0
    fadeDraw = 0

    healthDraw = []
    endScreenHealthDraw = []

    #Fade Sequence Meshes/Textures
    bitMaxes = [
        "gray12", "gray12", "gray12", "gray12", "gray12", "gray12", "gray12",
        "gray12", "gray25", "gray25", "gray25", "gray25", "gray25", "gray25",
        "gray25", "gray25", "gray50", "gray50", "gray50", "gray50", "gray50",
        "gray50", "gray50", "gray50", "gray75", "gray75", "gray75", "gray75",
        "gray75", "gray75", "gray75", "gray75", None, None, None, None, None,
        None, None, None
    ]

    xEscDoor = 0
    yEscDoor = 0

    lightFromDoor = "#101129"
    distFromDoor = 0

    escDoorPos = [[5, 60], [5, 135], [5, 210], [5, 285], [5, 360], [5, 435],
                  [5, 510], [866, 60], [866, 135], [866, 210], [866, 285],
                  [866, 360], [866, 435], [866, 510], [60, -1], [135, -1],
                  [210, -1], [285, -1], [360, -1], [435, -1], [510, -1],
                  [585, -1], [660, -1], [735, -1], [810, -1], [60, 570],
                  [135, 570], [210, 570], [285, 570], [360, 570], [435, 570],
                  [510, 570], [585, 570], [660, 570], [735, 570], [810, 570]]

    escDoorDraw = 0
    escPos = 0
    escDoorHeight = 0
    escDoorWidth = 0

    #Checkered Floor
    minX = 25
    minY = 25
    maxX = 100
    maxY = 100

    #Checkerboard Colours
    boardCols = ["#1A1B46", "#16173b"]
    col = 0

    #Images
    playImage = PhotoImage(file="play.gif")
    controlsImage = PhotoImage(file="controls.gif")
    loreImage = PhotoImage(file="lore.gif")
    playAgainImage = PhotoImage(file="playAgain.gif")
    menuImage = PhotoImage(file="menu.gif")
    gameLogoImage = PhotoImage(file="gameLogo.gif")
    quitImage = PhotoImage(file="quit.gif")
    levelsBelowImage = PhotoImage(file="levelsBelow.gif")
    levelNums = [
        PhotoImage(file="one.gif"),
        PhotoImage(file="two.gif"),
        PhotoImage(file="three.gif"),
        PhotoImage(file="four.gif"),
        PhotoImage(file="five.gif")
    ]
    charImages = [
        PhotoImage(file="charStr.gif"),
        PhotoImage(file="charBck.gif"),
        PhotoImage(file="charRht.gif"),
        PhotoImage(file="charLft.gif")
    ]
    heartImage = PhotoImage(file="heart.gif")
    crackImage = PhotoImage(file="crack.gif")
    webImage = PhotoImage(file="web.gif")
    crateImage = PhotoImage(file="crate.gif")
    excMarkImage = PhotoImage(file="excMark.gif")
    gameOvImages = [
        PhotoImage(file="gameOvL.gif"),
        PhotoImage(file="gameOvW.gif")
    ]
    escapeFuncImage = PhotoImage(file="escapeFunc.gif")
    gameControlsImage = PhotoImage(file="gameControls.gif")
    gameLoreInstImage = PhotoImage(file="gameLoreInst.gif")

    #Buttons
    controlButton = 0
    playButton = 0
    loreButton = 0
    menuButton = 0
    playAgainButton = 0
    quitButton = 0


#Draws Flooring
def drawScenery():
    global minX, maxX, minY, maxY, col, controlButton, playButton, loreButton

    #Checkerboard Rows
    for n in range(7):
        #Checkerboard Columns (Entire Row)
        for n in range(11):
            s.create_rectangle(minX,
                               minY,
                               maxX,
                               maxY,
                               fill=boardCols[col],
                               outline="")
            #Change Coordinates to Tile Immediately to the Right
            minX += 75
            maxX += 75
            #Change Colour
            col = ~col
        #Return to Initial 'X' Anchor Point
        minX = 25
        maxX = 100
        #Change Coordinates to Tile Immediately Underneath
        minY = maxY
        maxY += 75
    #Change Colour
    col = ~col


#Main Menu (Always Starts Here)
def mainMenu():

    s.delete("all")
    setInitialValues()

    #Draws Background/Menu Screen

    #Background Colour Scheme
    backgroundColours = ["#1f2162", "#1f2160"]
    backgroundY = 0

    #Draws Dark Background
    for i in range(2):
        s.create_rectangle(0,
                           backgroundY,
                           875,
                           backgroundY + 200,
                           fill=backgroundColours[i % 2],
                           outline="")
        backgroundY += 200

    #Building Anchor Points
    frontBuildingsX = 275
    backBuildingsX = 0

    #Building Width
    width = 0

    #Building Lengths
    frontBuildingsLength = [
        305, 330, 350, 325, 370, 360, 340, 380, 370, 390, 380
    ]
    backBuildingsLength = [
        355, 380, 400, 375, 420, 410, 390, 430, 420, 440, 430, 410, 380, 400,
        375, 370
    ]

    #Draws 'Back' Buildings (Lighter Purple)
    for i in range(15):

        #Draws Rectangle of Random Size
        if i == 0:
            width = 50
        else:
            width = randint(50, 125)
        s.create_rectangle(backBuildingsX,
                           600,
                           backBuildingsX + width,
                           600 - backBuildingsLength[i],
                           fill="#3f4181",
                           outline="")

        #Draws 'Dome' Roof
        if i % 2 != 0:
            s.create_arc(backBuildingsX - 1,
                         (600 - backBuildingsLength[i]) - 23,
                         backBuildingsX + width,
                         (600 - backBuildingsLength[i]) + 40,
                         start=0,
                         extent=180,
                         fill="#3f4181",
                         outline="")
            s.create_line(backBuildingsX + (width / 2),
                          (600 - backBuildingsLength[i]) - 20,
                          backBuildingsX + (width / 2),
                          (600 - backBuildingsLength[i]) - 30,
                          fill="#3f4181")
            s.create_polygon(backBuildingsX + (width / 2) - 17,
                             (600 - backBuildingsLength[i]) - 15,
                             backBuildingsX + (width / 2),
                             (600 - backBuildingsLength[i]) - 40,
                             backBuildingsX + (width / 2) + 17,
                             (600 - backBuildingsLength[i]) - 15,
                             fill="#3f4181")

        #Draws 'Conical' Roof
        elif i != 0 and i != 6:
            s.create_line(backBuildingsX - 2,
                          600 - backBuildingsLength[i],
                          backBuildingsX + width + 2,
                          600 - backBuildingsLength[i],
                          fill="#3f4181",
                          width=10)
            s.create_polygon(backBuildingsX,
                             600 - backBuildingsLength[i],
                             backBuildingsX + (width / 2),
                             600 - backBuildingsLength[i] - 30,
                             backBuildingsX + width,
                             600 - backBuildingsLength[i],
                             fill="#3f4181",
                             outline="")
        backBuildingsX += width

    #Draws 'Front' Buildings (Darker Purple)
    for i in range(10):

        #Draws Rectangle of Random Size
        width = randint(50, 100)
        s.create_rectangle(frontBuildingsX,
                           600,
                           frontBuildingsX + width,
                           600 - frontBuildingsLength[i],
                           fill="#101129",
                           outline="")

        #Draws 'Dome' Roof
        if i % 2 != 0:
            s.create_arc(frontBuildingsX - 1,
                         (600 - frontBuildingsLength[i]) - 23,
                         frontBuildingsX + width,
                         (600 - frontBuildingsLength[i]) + 40,
                         start=0,
                         extent=180,
                         fill="#101129",
                         outline="")
            s.create_line(frontBuildingsX + (width / 2),
                          (600 - frontBuildingsLength[i]) - 20,
                          frontBuildingsX + (width / 2),
                          (600 - frontBuildingsLength[i]) - 30,
                          fill="#101129")
            s.create_polygon(frontBuildingsX + (width / 2) - 16,
                             (600 - frontBuildingsLength[i]) - 15,
                             frontBuildingsX + (width / 2),
                             (600 - frontBuildingsLength[i]) - 35,
                             frontBuildingsX + (width / 2) + 16,
                             (600 - frontBuildingsLength[i]) - 15,
                             fill="#101129")

        #Draws 'Conical' Roof
        elif i != 0 and i != 6:
            s.create_line(frontBuildingsX - 2,
                          600 - frontBuildingsLength[i],
                          frontBuildingsX + width + 2,
                          600 - frontBuildingsLength[i],
                          fill="#101129",
                          width=10)
            s.create_polygon(frontBuildingsX,
                             600 - frontBuildingsLength[i],
                             frontBuildingsX + (width / 2),
                             600 - frontBuildingsLength[i] - 30,
                             frontBuildingsX + width,
                             600 - frontBuildingsLength[i],
                             fill="#101129",
                             outline="")
        frontBuildingsX += width

    #Arabian Mosque
    s.create_rectangle(0, 600, 250, 350, fill="#101129", outline="")
    s.create_arc(5,
                 250,
                 245,
                 500,
                 start=0,
                 extent=180,
                 fill="#101129",
                 outline="")
    s.create_arc(20,
                 260,
                 230,
                 470,
                 start=0,
                 extent=180,
                 fill="#1A1B46",
                 outline="")
    s.create_line(20, 395, 230, 395, fill="#1A1B46", width=2)
    s.create_line(20, 400, 230, 400, fill="#1A1B46", width=2)

    #Tower
    s.create_rectangle(245, 600, 275, 290, fill="#101129", outline="")
    s.create_rectangle(240, 280, 280, 290, fill="#101129", outline="")
    s.create_polygon(240, 290, 260, 240, 280, 290, fill="#101129", outline="")
    s.create_polygon(115, 245, 125, 220, 135, 245, fill="#101129", outline="")

    #Mosque 'Peak' (Arrow)
    s.create_line(260, 238, 260, 245, fill="#101129")
    s.create_line(125, 250, 125, 240, fill="#101129", width=10)

    #Arch Anchor Points
    archsX = 280
    archsY = 400

    #Draws Archs
    for i in range(10):
        s.create_rectangle(archsX,
                           archsY,
                           archsX + 50,
                           archsY - 50,
                           fill="#1A1B46",
                           outline="")
        s.create_arc(archsX,
                     archsY - 75,
                     archsX + 50,
                     archsY - 25,
                     start=0,
                     extent=180,
                     fill="#1A1B46",
                     outline="")
        archsX += 75

    #Arch Details (Lines Underneath/Above)
    s.create_line(280, 400, 855, 400, fill="#1A1B46", width=2)
    s.create_line(280, 404, 855, 404, fill="#1A1B46", width=2)
    s.create_line(295, 330, 845, 330, fill="#1A1B46", width=2)
    s.create_line(298, 326, 840, 326, fill="#1A1B46", width=2)

    #Initializing 'Star' Arrays
    starsX = []
    starsY = []
    stars = []
    starsSpeedX = []

    #Star Variables
    starsSize = [2, 3, 3.3]
    numOfStars = 100

    #Fills 'Star' Arrays w/ Values
    for i in range(numOfStars):
        starsX.append(randint(-50, 875))
        starsY.append(randint(0, 130))
        starsSpeedX.append(uniform(0.05, -0.05))
        stars.append(i)

    #Draws Stars
    for i in range(numOfStars):
        stars[i] = s.create_oval(starsX[i],
                                 starsY[i],
                                 starsX[i] + starsSize[i % 2],
                                 starsY[i] + starsSize[i % 2],
                                 fill="white",
                                 outline="")
        starsX[i] += starsSpeedX[i]

    #'Lights' Array; Off/On
    lights = ["#1A1B46", "white"]

    #Window Anchor Points
    leftWindowsX = 125
    rightWindowsX = 125

    #Window Width
    thickness = 10

    #Draws 'Windows' for Current Frame
    for i in range(6):
        s.create_line(leftWindowsX,
                      372,
                      leftWindowsX,
                      385,
                      fill=lights[i % 2],
                      width=thickness)
        s.create_line(rightWindowsX,
                      372,
                      rightWindowsX,
                      385,
                      fill=lights[i % 2],
                      width=thickness)
        leftWindowsX -= 12 + thickness
        rightWindowsX += 12 + thickness
        thickness -= 1

    #Draws Quit Statement
    s.create_image(430, 530, image=escapeFuncImage)

    #Logo Drawing
    s.create_image(437, 200, image=gameLogoImage)

    #Controls Button (Once Clicked, Provides Game Controls)
    controlButton = Button(s,
                           image=controlsImage,
                           borderwidth=0,
                           highlightthickness=0,
                           bg="#101129",
                           activebackground="#101129",
                           activeforeground="#101129",
                           command=controlsScreen)
    s.create_window(320, 450, window=controlButton, anchor=CENTER)

    #Play Button (Once Clicked, Runs Game)
    playButton = Button(s,
                        image=playImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        activeforeground="#101129",
                        command=runGame)
    s.create_window(450, 450, window=playButton, anchor=CENTER)

    #Lore Button (Once Clicked, Provides Game Lore/Instructions)
    loreButton = Button(s,
                        image=loreImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        activeforeground="#101129",
                        command=loreScreen)
    s.create_window(555, 450, window=loreButton, anchor=CENTER)


#Displays Game Controls
def controlsScreen():
    global menuButton

    s.delete("all")
    s.create_image(200, 65, image=gameControlsImage)
    s.create_text(
        438,
        325,
        text=
        "• CHARACTER MOVEMENT; use the LEFT MOUSE BUTTON to select any desired\ntile and the sprite will swiftly move to stand on it (if it is, of course, unoccupied)\nusing very basic pathfinding implementation; movement randomly alternates\nbetween ‘x-y’ and ‘y-x’ (for an added level of difficulty).\n\n• IMPORTANT NOTE; once a tile has been selected, all other attempts to change\nor relocate to another will not be addressed as the sprite begins to move (it\nmust be done after she has stopped, so choose wisely).\n\n• ESCAPE DOOR CONTROLS; upon discovering the hidden escape door for a\nparticular level, hit the ENTER key (when standing on the tile immediately in\nfront of it) to ascend.\n\n• BUTTONS; use the LEFT MOUSE BUTTON to click on any of the buttons.\n\n• QUIT; if and when you would like to quit, simply press the ESCAPE key.",
        fill="white",
        font="Helvetica 15 italic")

    #Menu Button (Once Clicked, Returns to Menu Screen)
    menuButton = Button(s,
                        image=menuImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        command=mainMenu)
    s.create_window(780, 65, window=menuButton, anchor=CENTER)


#Displays Game Lore/Instructions
def loreScreen():
    global menuButton

    s.delete("all")
    s.create_image(330, 74, image=gameLoreInstImage)
    s.create_text(
        430,
        331,
        text=
        "‘Ascent’ is a retro pixel puzzle game that takes place in the faraway land of Arcadia\nwhereby the main character (insert your name for her here; I can’t do everything)\nfinds herself in the underground (everchanging) levels of a relinquished ancient, but\nsomewhat alluring, building. Unaware of who she is nor how or why she has woken\nhere, her main aim is to escape; an unknown place is a dangerous place and it's\nevident that someone…or something is well in pursuit. She has discovered, upon\ncountless restless hours, that every floor has a discrete and concealed exit (only\npresenting itself when she is in close proximity), located on the very outer walls \n(deliberately designed by the original proprietor for reasons she would rather not\ncontemplate), encasing a flight of winding stairs that lead to the floor immediately\nabove. She has also discovered (unfortunately) just how ancient this building truly\nis; as she has, upon stepping on (numerous) weak cracks on the floor, fallen right\nthrough to the levels below. However, oddly enough, once she manages to ascend\nback up, the orientations of the rooms change entirely; crates, cracks, cobwebs,\nand all. Astonished, but terrified, by the architecture and inner workings of this\narcane place, she is driven to escape even faster... but is slowed down by the\nnumerous cobwebs; for a place that seems so ineffable, it sure is unkempt.\n\nGOAL: guide her through the last three levels by searching for the hidden exits while\navoiding potential cracks and falling down to the next level (as well as losing a heart).",
        fill="white",
        font="Helvetica 13 italic")

    #Menu Button (Once Clicked, Returns to Menu Screen)
    menuButton = Button(s,
                        image=menuImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        command=mainMenu)
    s.create_window(780, 58, window=menuButton, anchor=CENTER)


#Draws Cracks, Crates, and Cobwebs
def drawSpecTiles():
    global xCrack, yCrack, tilePosX, tilePosY, crackDraw, xCrackPos, yCrackPos, xWeb, yWeb, xWebPos, yWebPos, xCrate, yCrate, crateDraw, xCratePos, yCratePos, breakCue

    #Draws Cracks
    for i in range(numOfCracks):
        #Random Crack Position
        xCrack = choice(tilePosX)
        yCrack = choice(tilePosY)

        if xCrack == 435 and yCrack == 285:  #will not draw where the character begins (center tile)
            continue

        crackDraw = s.create_image(xCrack, yCrack,
                                   image=crackImage)  #draws cracks

        if i % 4 == 0:  #prevents a condensed area of cracks
            tilePosY.remove(yCrack)

        xCrackPos.append(xCrack)  #stores all crack 'x' positions
        yCrackPos.append(yCrack)  #stores all crack 'y' positions

    #Initializing Variable to Manipulate
    breakCue = False

    #Draws Cobwebs
    for i in range(numOfWebs):
        #Random Cobweb Position
        xWeb = choice(tilePosX)
        yWeb = choice(tilePosY)

        if xWeb == 435 and yWeb == 285:  #will not draw where the character begins (center tile)
            continue

        elif (
                xWeb == 60 or xWeb == 135
        ) and yWeb == 60:  #will not draw in top left corner (for visual purposes)
            continue

        for i in range(len(xCrackPos)):
            if xWeb == xCrackPos[i] and yWeb == yCrackPos[
                    i]:  #prevents a cobweb drawn on top of a crack
                breakCue = True

        if breakCue == False:  #draws cobwebs and stores their positions
            crackDraw = s.create_image(xWeb, yWeb, image=webImage)
            xWebPos.append(xWeb)
            yWebPos.append(yWeb)

        if i % 2 == 0:  #prevents a condensed area of cobwebs
            tilePosX.remove(xWeb)

        breakCue = False

    #Initializing Variable to Manipulate
    breakCue = False

    #Draws Crates
    for i in range(numOfCrates):
        if len(cratePosX) == 0 or len(
                cratePosY
        ) == 0:  #prevents crates being drawn when no tiles available
            break

        #Random Crate Position
        xCrate = choice(cratePosX)
        yCrate = choice(cratePosY)

        if xCrate == 435 and yCrate == 285:  #will not draw where the character begins (center tile)
            continue

        elif xCrate == 435 and yCrate == 210:  #will not trap the character in the middle
            continue

        for i in range(len(xCrackPos)):
            if xCrate == xCrackPos[i] and yCrate == yCrackPos[
                    i]:  #prevents a crate drawn on top of a crack
                breakCue = True

        for i in range(len(xWebPos)):
            if xCrate == xWebPos[i] and yCrate == yWebPos[
                    i]:  #prevents a crate drawn on top of a cobweb
                breakCue = True

        if breakCue == False:  #draws crates and stores their positions
            crateDraw = s.create_image(xCrate, yCrate, image=crateImage)
            xCratePos.append(xCrate)
            yCratePos.append(yCrate)

        if i % 5 == 0:  #prevents a condensed area of crates
            cratePosX.remove(xCrate)

        breakCue = False


#Declaring 'Weak' Cracks
def createCrackedTile():
    global typeOfTile, chanceOfBroken

    #Declares if Crack is Weak
    for i in range(len(xCrackPos)):
        chanceOfBroken = [0] * 7 + [1] * 5

        #Prevents Character From Experiencing 'Weak' Cracks Directly in Front of Escape Door
        if sqrt((xEscDoor - xCrackPos[i])**2 +
                (yEscDoor - yCrackPos[i])**2) <= 62:
            typeOfTile.append(0)

        else:
            typeOfTile.append(choice(chanceOfBroken))


#Initializes Escape Door
def createEscapeDoor():
    global xEscDoor, yEscDoor, escDoorHeight, escDoorWidth, escPos

    #Chooses Position for Escape Door (Outer Walls)
    escPos = choice(escDoorPos)
    xEscDoor = escPos[0]
    yEscDoor = escPos[1]

    #Initializes Door 'Attributes' (Draws Correct Orientation)
    if xEscDoor == 5:
        escDoorHeight += -35
        escDoorWidth += 10

    elif xEscDoor == 866:
        escDoorHeight += -35
        escDoorWidth += 10

    elif yEscDoor == 570:
        escDoorWidth += -35
        escDoorHeight += 10

    else:
        escDoorWidth += -35
        escDoorHeight += 15


#Creates Health Bar
def createHealthBar():
    global xHealthPos, healthDraw, xHealth

    #Initializes Position of Hearts
    for i in range(health):
        xHealthPos.append(xHealth)
        healthDraw.append(i)
        xHealth += 41


#Draws Character, Health Bar, Escape Door, and Level Number
def drawObjects():
    global charDraw, healthDraw, escDoorDraw, levelsBelowDraw, levelNumDraw

    #Draws Character
    charDraw = s.create_image(xChar, yChar, image=charImages[charImageIndex])

    #Draws Health Bar
    for i in range(health):
        healthDraw[i] = s.create_image(xHealthPos[i],
                                       yHealth,
                                       image=heartImage)

    #Draws Escape Door (Hidden at First)
    escDoorDraw = s.create_rectangle(xEscDoor + escDoorWidth,
                                     yEscDoor + escDoorHeight,
                                     xEscDoor - escDoorWidth + 5,
                                     yEscDoor - escDoorHeight,
                                     fill=lightFromDoor,
                                     outline=lightFromDoor,
                                     width=5)

    #Draws 'Levels Below Ground' Text
    levelsBelowDraw = s.create_image(125, 7, image=levelsBelowImage)

    #Draws Number of Levels Below Ground
    if floorLvl == -5:  #formatting; properly aligns all of the numbers
        levelNumDraw = s.create_image(233,
                                      6,
                                      image=levelNums[abs(floorLvl) - 1])

    else:  #formatting; properly aligns all of the numbers
        levelNumDraw = s.create_image(233,
                                      5,
                                      image=levelNums[abs(floorLvl) - 1])


#Updates Object Positions
def updateObjects():
    global xChar, yChar, charImageIndex, prevClick

    #Moves Character According to Random Movement Order
    if wayOfMovement == 1:  #moves the character on the x-axis first, then the y-axis

        if xChar != xFinalTile and xSpeed != 0:  #moves the character until they have reached the chosen tile's 'x' position
            xChar += xSpeed

            #Character Profile Formatting
            if xSpeed > 0:
                charImageIndex = 2
            elif xSpeed < 0:
                charImageIndex = 3

            prevClick = True  #declaring that the previous click is still being addressed

        elif yChar != yFinalTile and ySpeed != 0:  #moves the character until they have reached the chosen tile's 'y' position
            yChar += ySpeed

            #Character Profile Formatting
            charImageIndex = 0 if ySpeed > 0 else 1

            prevClick = True  #declaring that the previous click is still being addressed

        #Defaults to Character Facing Forward
        else:  #when the character has stopped moving
            charImageIndex = 0
            prevClick = False  #declaring that the previous click is done being addressed

    else:  #moves the character on the y-axis first, then the x-axis

        if yChar != yFinalTile and ySpeed != 0:  #moves the character until they have reached the chosen tile's 'y' position
            yChar += ySpeed

            #Character Profile Formatting
            charImageIndex = 0 if ySpeed > 0 else 1

            prevClick = True  #declaring that the previous click is still being addressed

        elif xChar != xFinalTile and xSpeed != 0:  #moves the character until they have reached the chosen tile's 'x' position
            xChar += xSpeed

            #Character Profile Formatting
            if xSpeed > 0:
                charImageIndex = 2
            elif xSpeed < 0:
                charImageIndex = 3

            prevClick = True  #declaring that the previous click is still being addressed

        #Defaults to Character Facing Forward
        else:  #when character has stopped moving
            charImageIndex = 0
            prevClick = False  #declaring that the previous click is done being addressed


#Collision Check
def checkForCollisions():
    global charSpeed, xSpeed, ySpeed, xFinalTile, yFinalTile, excMarkDraw, fallenCase, nextTileX, nextTileY

    #Predicts Next Tile Character Goes to (According to Path)
    nextTileX = ((floor(((xChar + xSpeed) - 25) / 75)) * 75) + 35 + 25
    nextTileY = ((floor(((yChar + ySpeed) - 25) / 75)) * 75) + 35 + 25

    #Prevents Character From Going Through Crates
    for i in range(
            len(xCratePos)):  #animates the character bumping into the crates
        if nextTileX == xCratePos[i] and nextTileY == yCratePos[i]:
            xFinalTile = xChar - (np.sign(nextTileX - xChar)) * 35
            yFinalTile = yChar - (np.sign(nextTileY - yChar)) * 35
            break

    #Initializing Variables to Manipulate
    charSpeed = 5
    xSpeed = np.sign(xFinalTile - xChar)
    ySpeed = np.sign(yFinalTile - yChar)

    #Slows Character Down on Cobwebs
    for i in range(len(xWebPos)):
        if xWebPos[i] - 35 < xChar < xWebPos[i] + 35 and yWebPos[
                i] - 35 < yChar < yWebPos[i] + 35:
            charSpeed /= 10
            break

            #Updates Character Speed
    xSpeed *= charSpeed
    ySpeed *= charSpeed

    #Initializing Variables to Manipulate
    xSpeed = np.sign(xFinalTile - xChar)
    ySpeed = np.sign(yFinalTile - yChar)

    #Animates Falling Sequence
    for i in range(len(xCrackPos)):
        if xCrackPos[i] == xChar and yCrackPos[i] == yChar:

            #Character Stepped on Weak Crack
            if typeOfTile[i] == 1:
                charSpeed *= 0  #prevents character from moving
                excMarkDraw = s.create_image(xChar + 40,
                                             yChar - 40,
                                             image=excMarkImage)

                drawObjects()
                s.update()

                #Character Profile Formatting
                if charImageIndex != 0:
                    sleep(0.75)

                s.delete(charDraw, escDoorDraw, levelsBelowDraw, levelNumDraw)
                for i in range(health):
                    s.delete(healthDraw[i])

                #Initiates 'Descend' Sequence
                fallenCase = True

    #Updates Character Speed
    xSpeed *= charSpeed
    ySpeed *= charSpeed


#Escape Door Interactions Check
def doorInteractionCheck():
    global distFromDoor, lightFromDoor, charAscend, charImageIndex

    #Determines Character's Distance From Door
    distFromDoor = sqrt((xEscDoor - xChar)**2 + (yEscDoor - yChar)**2)

    #Character is Directly in Front of Door
    if distFromDoor <= 62 and xChar == xFinalTile and yChar == yFinalTile:

        #Redraws Objects
        drawObjects()
        s.update()
        sleep(0.03)
        s.delete(charDraw, escDoorDraw, levelsBelowDraw, levelNumDraw)
        for i in range(health):
            s.delete(healthDraw[i])

        #User has Clicked 'Enter'
        if ascendBool == True:

            sleep(0.25)

            #Changes Door Light (Brighter; Character is Entering)
            lightFromDoor = "#CCCDD9"

            #Initiates 'Ascend' Sequence
            charAscend = True

    #Gradually Reveals Escape Door as Character is in Vicinity
    elif distFromDoor <= 65:
        lightFromDoor = "#86879C"
    elif distFromDoor <= 70:
        lightFromDoor = "#6E6F85"
    elif distFromDoor <= 80:
        lightFromDoor = "#53546B"
    elif distFromDoor <= 90:
        lightFromDoor = "#3B3C54"
    elif distFromDoor <= 100:
        lightFromDoor = "#101129"


#Fades Screen to Black
def fadeInSeq():
    global fadeDraw

    for i in range(40):  #gradually shifts through the meshes
        fadeDraw = s.create_rectangle(0,
                                      0,
                                      875,
                                      575,
                                      fill="black",
                                      stipple=bitMaxes[i])
        s.update()
        sleep(0.03)
        s.delete(fadeDraw)


#Fades Screen out of Black
def fadeOutSeq():
    global fadeDraw

    for i in reversed(
            range(40)):  #gradually shifts backwards through the meshes
        fadeDraw = s.create_rectangle(0,
                                      0,
                                      875,
                                      575,
                                      fill="black",
                                      stipple=bitMaxes[i])
        s.update()
        sleep(0.03)
        s.delete(fadeDraw)


#'Ascends' User to Next Upper Level
def ascendSeq():
    global floorLvl

    #Fade Sequence
    sleep(1)
    fadeInSeq()
    s.delete("all")
    floorLvl += 1

    #Draws New Level/Room
    if floorLvl != 0:
        setInitialValues()
        drawScenery()
        drawSpecTiles()
        createEscapeDoor()
        createHealthBar()
        createCrackedTile()
        drawObjects()
        sleep(1)
        s.update()


#'Descends' User to Next Lower Level
def descendSeq():
    global health, floorLvl

    #Fade Sequence
    drawObjects()
    s.update()
    sleep(0.75)
    fadeInSeq()

    s.delete("all")
    health -= 1
    floorLvl -= 1

    #Draws New Room/Level
    if health != 0:
        setInitialValues()
        drawScenery()
        drawSpecTiles()
        createEscapeDoor()
        createHealthBar()
        createCrackedTile()
        drawObjects()
        sleep(1)
        s.update()


#Mouse Click Handler
def mouseClickHandler(event):
    global xMouse, yMouse, xFinalTile, yFinalTile, wayOfMovement, click

    #Mouse Coordinates
    xMouse = event.x
    yMouse = event.y

    #Prevents Character From Moving Beyond the Border
    if xMouse < 25:  #moves character to nearest tile (if mouse click is beyond the border)
        xMouse += 25
    elif xMouse > 845:
        xMouse -= 25
    if yMouse < 25:
        yMouse += 25
    elif yMouse > 550:
        yMouse -= 25

    #Prevents User From Moving When Character is in Motion (Prevents Relocation Midway)
    if prevClick == False:
        xFinalTile = ((floor(
            (xMouse - 25) / 75)) * 75) + 35 + 25  #border width
        yFinalTile = ((floor(
            (yMouse - 25) / 75)) * 75) + 35 + 25  #border width
        wayOfMovement = randint(0, 1)

    #Declaring Variable to Manipulate
    click = True


#Key Press Handler
def keyDownHandler(event):
    global ascendBool, exiting

    #User Enters Escape Door
    if event.keysym == "Return":
        ascendBool = True

    #User Quits Game
    if event.keysym == "Escape":
        if gameRun == False:
            quit()
        else:
            exiting = True


#Key Release Handler
def keyUpHandler(event):
    global ascendBool

    #Prevents User From Ascending When Not Near Escape Door
    if event.keysym == "Return":
        ascendBool = False


#End Game Screen
def endGame():
    global gameOverDraw, xEndScreenHealth, yEndScreenHealth, menuButton, playAgainButton, quitButton

    sleep(0.25)
    s.delete("all")

    #Loss Message/Screen
    if health <= 0:
        gameOverDraw = s.create_image(440, 220, image=gameOvImages[0])

    #Win Message/Screen
    else:
        gameOverDraw = s.create_image(445, 310, image=gameOvImages[1])
        yEndScreenHealth -= 120

    #Menu Button (Once Clicked, Returns to Menu Screen)
    menuButton = Button(s,
                        image=menuImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        activeforeground="#101129",
                        command=mainMenu)
    s.create_window(310, 415, window=menuButton, anchor=CENTER)

    #Play Again Button (Once Clicked, Runs New Game)
    playAgainButton = Button(s,
                             image=playAgainImage,
                             borderwidth=0,
                             highlightthickness=0,
                             bg="#101129",
                             activebackground="#101129",
                             activeforeground="#101129",
                             command=runGame)
    s.create_window(441, 415, window=playAgainButton, anchor=CENTER)

    #Quit Button (Once Clicked, Quits Game)
    quitButton = Button(s,
                        image=quitImage,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#101129",
                        activebackground="#101129",
                        activeforeground="#101129",
                        command=quit)
    s.create_window(565, 415, window=quitButton, anchor=CENTER)

    #Draws Decorative Hearts

    for i in range(endScreenHealth):
        xEndScreenHealthPos.append(xEndScreenHealth)
        endScreenHealthDraw.append(i)
        xEndScreenHealth += 75

    endScreenHealthDraw[0] = s.create_image(xEndScreenHealthPos[0],
                                            yEndScreenHealth,
                                            image=heartImage)
    endScreenHealthDraw[1] = s.create_image(xEndScreenHealthPos[1],
                                            yEndScreenHealth,
                                            image=heartImage)
    endScreenHealthDraw[2] = s.create_image(xEndScreenHealthPos[2],
                                            yEndScreenHealth,
                                            image=heartImage)
    s.update()


#Runs Game (Directs Flow)
def runGame():

    sleep(0.5)
    s.delete("all")
    setInitialValues()
    setInitialStats()
    drawScenery()
    drawSpecTiles()
    createEscapeDoor()
    createHealthBar()
    createCrackedTile()

    #While User Has Not Quit, Lost, Nor Won
    while gameRun == True and health >= 1 and floorLvl < 0:
        drawObjects()

        if fallenCase == True:  #character has stepped on a weak crack
            descendSeq()

            if health == 0:  #user has lost all health
                sleep(1)
                break

            fadeOutSeq()

        if charAscend == True:  #character has entered escape door
            ascendSeq()

            if floorLvl == 0:  #user has reached ground level
                sleep(1)
                break

            fadeOutSeq()

        s.update()
        sleep(0.03)
        s.delete(charDraw, escDoorDraw, levelsBelowDraw, levelNumDraw)

        for i in range(health):
            s.delete(healthDraw[i])

        #User has Interacted w/ Screen
        if click == True:
            checkForCollisions()  #checks for collisions

        updateObjects()
        doorInteractionCheck()  #escape door interaction check

        if exiting == True:  #user quits
            quit()

    endGame()  #game has ended


#Configurations

root.after(0, mainMenu)

s.bind("<Button-1>", mouseClickHandler)
s.bind("<Key>", keyDownHandler)
s.bind("<KeyRelease>", keyUpHandler)

s.pack()
s.focus_set()
root.mainloop()
