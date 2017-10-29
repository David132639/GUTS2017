import Tkinter
from Tkinter import *
import time
import random
import socket
from threading import Thread
from PIL import ImageTk
import pygame

from newgame import *
import monstercreator
import monster
import wallcreator

pygame.mixer.init()
pygame.mixer.music.load("res/music.mp3")
pygame.mixer.music.play(-1)

top = Tkinter.Tk()

####################### Network staff
m = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with open("ip.txt") as f:
    opponent = f.readline().strip()
print opponent


def send(msg):  # Send message to other computer
    m.sendto(msg, (str(opponent), 5505))


def listen():
    r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    r.bind(("0.0.0.0", 5505))
    while True:
        data, addr = r.recvfrom(1024)
        keypressForeign(data)
    r.close


def keypressLocal(event):
    send(event.keysym)


def keypressForeign(data):  # Process incoming messsage
    print data
    global updateNextButton
    global level
    global goToNextLevel
    if data == 'Up' or data == 'w':
        turnUp()
        stop()
    if data == 'Down' or data == 's':
        turnDown()
        stop()
    if data == 'Left' or data == 'a':
        turnLeft()
        stop()
    if data == 'Right' or data == 'd':
        turnRight()
        stop()
    if data == 'xDead':
        global lives
        lives -= 1
        if lives == 0:
            dead()
        print "Partner hit a monster", str(lives)
        newloc = (1, 1)
    if data == 'xOneFinished':
        global otherFinished
        otherFinished = True
    if data == 'xAllFinished':
        updateNextButton = True
    if data[:8] == 'xLevelUp':
        if int(data[8:]) != level:
            goToNextLevel = True
            print goToNextLevel, "Test1"


top.bind("<Key>", keypressLocal)
list = Thread(target=listen)
list.daemon = True
list.start()
#######################

# Initialize images
##Changed pictures 1.31 SOHVA
grass = ImageTk.PhotoImage(file="res/background.png")
foodimage = ImageTk.PhotoImage(file="res/spiderBG.png")
pumpkinImage = ImageTk.PhotoImage(file="res/pumpkin2BG.png")
happyImage = ImageTk.PhotoImage(file="res/happy_pumpkinBG.png")
scaredImage = ImageTk.PhotoImage(file="res/pumpkin_scaredBG.png")
monsterImages = [ImageTk.PhotoImage(file="res/ghostBG.png"), \
                 ImageTk.PhotoImage(file="res/batBG.png"), \
                 ImageTk.PhotoImage(file="res/82872-200BG.png"), \
                 ImageTk.PhotoImage(file="res/mouseBG.png")]
monsterImage = monsterImages[random.randint(0, len(monsterImages) - 1)]
trophy = ImageTk.PhotoImage(file="res/trophyBG.png")
grave = ImageTk.PhotoImage(file="res/graveBG.png")


# Creates the initial pumpkin
def createPumpkin():
    global pumpkin
    ##SNAKE MODIFIED 1.1 SOHVA
    pumpkin = (1, 1)

def newGame():
    global monsterImage
    global monsterImages
    global pumpkin
    global sGrid
    global food
    global columns
    global rows
    global game_on
    global direction
    global new_direction
    global foodlist
    global level
    global lives

    lives = 5
    liveslabel.configure(text = "You have "+str(lives)+" attempts")
    monsterImage = monsterImages[random.randint(0,len(monsterImages)-1)]

    level = 1
    sGrid[pumpkin[0]][pumpkin[1]].configure(image = pumpkinright)
    createPumpkin()
    foodlist=[]
    #get_score()
    for row in sGrid:
        for item in row:
            item.configure(image = grass, bg = "grey")

    global numFood
    numFood = random.randint(1,3)
    for i in range (0, numFood):
        addFood()
        foodlist.append(food)
    for food in foodlist:
        sGrid[food[0]][food[1]].configure(image = foodimage)

    game_on = True
    direction = (0,-1)
    new_direction = (0,-1)
    levellabel.configure(text = "Level: " + str(level))


def addFood():
    global pumpkin
    global sGrid
    global food
    global columns
    global rows
    global foodlist
    while True:
        # Choses a random location
        chosen = (random.randint(2, rows - 3), random.randint(2, columns - 3))
        # Checks that it's not in the pumpkin
        monLocs = giveMonLocs(monsters)
        if chosen != pumpkin and chosen not in walls and chosen != finish and chosen not in monLocs:
            food = chosen
            foodlist.append(food)
            break





def game():
    global otherFinished
    global goToNextLevel
    global pumpkin
    global direction
    global game_on
    global highscore
    global numFood
    global foodlist
    global updateNextButton

    global level
    createWalls(level)
    global lives
    global moves
    global movesOnce

    statelabel.configure(text="Have not won/lost yet.")

    ##Adding monsters 1.3 SOHVA
    global monsters

    ##Adding finish 1.4 Sohva
    global finish

    ##Adding wall 1.5 Sohva
    global walls
    sGrid[finish[0]][finish[1]].configure(image=trophy)
    game_on = True
    for monster in monsters:
        monloc = monster.getLoc()
        sGrid[monloc[0]][monloc[1]].configure(image=grass)
        monster.move()
        monloc = monster.getLoc()
        sGrid[monloc[0]][monloc[1]].configure(image=monsterImage)

    loc = pumpkin
    # Update the location
    if moves or movesOnce:
        newloc = ((loc[0] + direction[0]) % rows, (loc[1] + direction[1]) % columns)
        movesOnce = False
        for wall in walls:
            if newloc == wall:
                newloc = loc
    else:
        newloc = loc

    ##Check for the collision with monster 1.3 SOHVA
    for monster in monsters:
        if newloc == monster.getLoc():
            lives -= 1
            refreshLives()
            if lives == 0:
                dead()
            send("xDead")
            print "Hit a monster"
            newloc = (1, 1)

    if newloc == finish:
        send("xOneFinished")

        ###FOR TESTING
        # otherFinished = True
        ###

        if otherFinished == True:
            send("xAllFinished")
            nextButton.configure(state="normal")
            win()

        print "Game nearly Won!"

    for i in range(len(foodlist)):
        if newloc == foodlist[i]:
            lives -= 1
            refreshLives()
            if lives == 0:
                dead()
            nextloc = newloc[0] - direction[0], newloc[1] - direction[1]
            while nextloc not in walls:
                newloc = nextloc
                nextloc = newloc[0] - direction[0], newloc[1] - direction[1]

    sGrid[pumpkin[0]][pumpkin[1]].configure(image=grass)
    pumpkin = newloc

    # Make the head to point to the right direction
    nextloc = (newloc[0] + direction[0], newloc[1] + direction[1])
    nextLocs = giveNextLocs(pumpkin)
    pumpkinhead = pumpkinImage
    if finish in nextLocs or newloc == finish:
        pumpkinhead = happyImage
    else:
        for loc in nextLocs:
            if loc in foodlist:
                pumpkinhead = scaredImage
                break
        for monster in monsters:
            if monster.getLoc() in nextLocs:
                pumpkinhead = scaredImage
                break

    sGrid[newloc[0]][newloc[1]].configure(image=pumpkinhead)

    if goToNextLevel:
        levelUp()
        goToNextLevel = False

    if updateNextButton:
        nextButton.configure(state="normal")
        updateNextButton = False


##Version 1.2 SOHVA ADDED MOVES VARIABLE FOR DECIDING WHETHER PLAYER MOVES OR NOT
##Version 1.22 SOHVA FIXED A BUG WITH THE SNAKE MOVEMENT
def turnRight():
    global direction
    global new_direction
    global moves
    global movesOnce

    new_direction = (0, 1)
    moves = True
    movesOnce = True


def turnLeft():
    global direction
    global new_direction
    global moves
    global movesOnce
    new_direction = (0, -1)
    moves = True
    movesOnce = True


def turnUp():
    global direction
    global new_direction
    global moves
    global movesOnce
    new_direction = (-1, 0)
    moves = True
    movesOnce = True


def turnDown():
    global direction
    global new_direction
    global moves
    global movesOnce
    new_direction = (1, 0)
    moves = True
    movesOnce = True


def pause():
    global game_on
    game_on = not game_on


##VERSION 1.2 SOHVA STOPS PLAYER MOVEMENT
def stop():
    global moves
    moves = False


def createWalls(level):
    global walls
    walls = []
    walls = wallcreator.createWalls(level)
    for wall in walls:
        sGrid[wall[0]][wall[1]].configure(image=grave)


def levelUp():
    global otherFinished
    global nextButton
    otherFinished = False
    global foodlist
    global walls
    global monsters
    global level
    global pumpkin
    global monsterImage
    global monsterImages

    monsterImage = monsterImages[random.randint(0, len(monsterImages) - 1)]

    for row in sGrid:
        for square in row:
            square.configure(image=grass)
    nextButton.config(state="disabled")
    game_on = True
    pumpkin = (1, 1)
    level += 1
    send("xLevelUp" + str(level))
    levellabel.configure(text="Level: " + str(level))
    monsters = createMonsters(level)
    createWalls(level)
    foodlist = []
    addFood()
    for food in foodlist:
        sGrid[food[0]][food[1]].configure(image=foodimage)

    nextButton.configure(state="disabled")


# Gives the locations in which the monsters can be
def giveMonLocs(monsters):
    locs = []
    for monster in monsters:
        locs += monster.getRoute()
    return locs


def giveNextLocs(pumpkin):
    return [(pumpkin[0] - 1, pumpkin[1]), (pumpkin[0] + 1, pumpkin[1]), \
            (pumpkin[0], pumpkin[1] - 1), (pumpkin[0], pumpkin[1] + 1)]

def createMonsters(level):
        global monsters
        monsters = monstercreator.createMonsters(level)
lives = 5
liveslabel = Tkinter.Label(top, text=str(lives) + " lives left")

def refreshLives():
    global liveslabel
    global lives
    liveslabel.config(text=str(lives) + " lives left")
    
columns = 15
rows = 10
game_on = True
pumpkin = []
highscore = 0
foodlist = []
finish = (rows - 3, columns - 3)
walls = []

refreshLives()



    
liveslabel.grid(row=0, columnspan=5, column=4)
statelabel = Tkinter.Label(top, text="Have not won/lost yet.")
statelabel.grid(row=0, columnspan=6, column=9)

# Create the grid
sGrid = []
for rownum in range(rows):
    row = []
    for colnum in range(columns):
        label = Tkinter.Label(top, image=grass, bg="#6d6764", bd=0)
        row += [label]
        label.grid(row=rownum + 1, column=colnum)
    sGrid += [row]

createPumpkin()

createMonsters(1)

##1.6 SOHVA adds the variable for level
level = 1

levellabel = Tkinter.Label(top, text="Level: " + str(level))
levellabel.grid(row=0, columnspan=5, column=0)

createWalls(1)

# Place the food
addFood()
for food in foodlist:
    sGrid[food[0]][food[1]].configure(image=foodimage)

# Tells how to change coordinates
# up = (1,0); down = (-1,0); left = (0,-1); right = (0,1)
direction = (0, -1)  # Left
new_direction = (0, -1)

## VERSION 1.2 SOHVA a boolean for the player movement
moves = False
movesOnce = False

otherFinished = False

updateNextButton = False
goToNextLevel = False

quitButton = Tkinter.Button(top, text="Quit", command=top.destroy)
quitButton.grid(row=0, column=columns + 1, rowspan=2)
newButton = Tkinter.Button(top, text="New Game", command=newGame)
newButton.grid(row=1, column=columns + 1, rowspan=2)
nextButton = Tkinter.Button(top, text="Next Level", command=levelUp, state="disabled")
nextButton.grid(row=2, column=columns + 1, rowspan=2)


# Keeps track on the level

def dead():
    global game_on
    global statelabel
    if game_on:
        game_on = False
        statelabel.configure(text="You lost. Try again!")


def win():
    # global game_on
    global statelabel
    statelabel.configure(text="You won. Try next level!")


while True:
    if game_on:
        game()

    for i in range(10):
        time.sleep((0.35 - level * 0.05) / 10)
        top.update_idletasks()
        top.update()
    direction = new_direction
