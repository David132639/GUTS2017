##Version 1.7 Marija count
import Tkinter
from Tkinter import *
import time
import random
import socket
from threading import Thread
from PIL import ImageTk

##Adds walls
import wallcreator

top=Tkinter.Tk()

####################### Network staff
m=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
with open("ip.txt") as f:
    opponent=f.readline().strip()
print opponent
def send(msg): # Send message to other computer
    m.sendto(msg,(str(opponent),5501))
def listen():
    r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.bind(("0.0.0.0",5501))
    while True:
            data,addr=r.recvfrom(1024)
            keypress_foreign(data)
    r.close
def keypress_local(event):
    m.sendto(event.keysym,(str(opponent),5501))
def keypress_foreign(data): # Process incoming messsage
    print data
    global nextButton
    if data=='Up' or data=='w':
        turnUp()
        stop()
    if data=='Down' or data=='s':
        turnDown()
        stop()
    if data=='Left' or data=='a':
        turnLeft()
        stop()
    if data=='Right' or data=='d':
        turnRight()
        stop()
    if data=='xDead':
        print "Partner hit a monster"
        newloc = (1,1)
    if data=='xOneFinished':
        global otherFinished
        otherFinished=True
    if data=='xAllFinished':
        nextButton.configure(state="normal")
        send("xAllFinished")
        pause()
top.bind("<Key>",keypress_local)
list=Thread(target=listen)
list.daemon=True
list.start()
#######################

##Importing monster 1.3 SOHVA
import monstercreator
import monster

#Initialize images
##Changed pictures 1.31 SOHVA
grass = ImageTk.PhotoImage(file = "background.png")
foodimage = ImageTk.PhotoImage(file = "spider.png")
snakeskin = ImageTk.PhotoImage(file = "snake.png")
snakeleft = ImageTk.PhotoImage(file = "pumpkin2.png")
snakeup = ImageTk.PhotoImage(file = "pumpkin2.png")
snakeright = ImageTk.PhotoImage(file = "pumpkin2.png")
snakedown = ImageTk.PhotoImage(file = "pumpkin2.png")
snakelefteat = ImageTk.PhotoImage(file = "happy_pumpkin.png")
snakeupeat = ImageTk.PhotoImage(file = "happy_pumpkin.png")
snakerighteat = ImageTk.PhotoImage(file = "happy_pumpkin.png")
snakedowneat = ImageTk.PhotoImage(file = "happy_pumpkin.png")
monsterImage = ImageTk.PhotoImage(file = "ghost.png")

##Adding finish 1.4 Sohva
trophy = ImageTk.PhotoImage(file = "trophy.png")

##Adding wall 1.5 SOHVA
grave = ImageTk.PhotoImage(file = "grave.png")

def get_score():
    global highscore
    scores = open("snake_high_score.txt","r")
    highscore = int(scores.readline())
    scores.close()

#Creates the initial snake    
def createSnake():
    global snake
    global sGrid
    ##SNAKE MODIFIED 1.1 SOHVA
    snake = (1,1)

def newGame():
    global snake
    global sGrid
    global food
    global columns
    global rows
    global game_on
    global direction
    global new_direction
    global foodlist
    global level
    foodlist=[]
    get_score()
    for row in sGrid:
        for item in row:
            item.configure(image = grass, bg = "grey")
    createSnake()
    global numFood
    numFood = random.randint(1,3)
    for i in range (0, numFood):
        addFood()
        foodlist.append(food)
    
    game_on = True
    direction = (0,-1)
    new_direction = (0,-1)
    levellabel.configure(text = "Level: " + str(level))
    
def addFood():
    global snake
    global sGrid
    global food
    global columns
    global rows
    global foodlist
    foodlist = []
    while True:
        #Choses a random location
        chosen = (random.randint(2,rows-3),random.randint(2,columns-3))
        #Checks that it's not in the snake
        if chosen != snake and chosen not in walls:
            food = chosen
            foodlist.append(food)
            sGrid[food[0]][food[1]].configure(image = foodimage)
            break
    
    
def game():
    global otherFinished
    #Makes the snake move
    global snake
    global direction
    global game_on
    global highscore
    global numFood
    global foodlist

    global level
    createWalls(level)
    
    #foodlist=[]
    ## SNAKE CHANGED 1.1 S
    ## SNAKE MOVING CHANGED 1.2 SOHVA
    global moves
    global movesOnce

    ##Adding monsters 1.3 SOHVA
    global monsters

    ##Adding finish 1.4 Sohva
    global finish

    ##Adding wall 1.5 Sohva
    global walls
    sGrid[finish[0]][finish[1]].configure(image = trophy)

    for monster in monsters:
        monloc = monster.getLoc()
        sGrid[monloc[0]][monloc[1]].configure(image = grass)
        monster.move()
        monloc = monster.getLoc()
        sGrid[monloc[0]][monloc[1]].configure(image = monsterImage)

        

    
    loc = snake
    #Update the location
    if moves or movesOnce:
        newloc = ((loc[0]+direction[0])%rows,(loc[1]+direction[1])%columns)
        movesOnce = False
        for wall in walls:
            if newloc == wall:
                newloc = loc
    else:
        newloc = loc

    ##Check for the collision with monster 1.3 SOHVA
    for monster in monsters:
        if newloc == monster.getLoc():
            send("xDead")
            print "Hit a monster"
            newloc = (1,1)

    if newloc == finish:
        send("xOneFinished")

##        ###FOR TESTING
##        otherFinished = True
##        ###
        if otherFinished==True:
            send("xAllFinished")

        print "Game nearly Won!"
##1.7 Commented out
##        root = Tk()
##        label = Label(root, text="Game nearly Won!")
##        label.pack()
##        root.mainloop()

        #print "Game nearly Won!"

## COMMENTED OUT 1.1 SOHVA
##    if newloc in snake:
##        #If we hit the snake, the game is over
##        game_on = False
##        for item in snake:
##            sGrid[item[0]][item[1]].configure(bg = "red")
##            if len(snake) - 4 > highscore:
##                scores = open("snake_high_score.txt","w")
##                scores.write(str(len(snake)-4))
##                scores.close()
##    elif newloc == food:
##        #If we hit food, the snake won't get shorter and the location of food is changed
##        snake += [newloc]
##        addFood()
##        levellabel.configure(text = "Level: " + str(len(snake)-4))
##        if len(snake) - 4 > highscore:
##            scorelabel.configure(text = "Record: " + str(len(snake)-4))
##    else:
        #The tail of the snake is removed and the new location added
        ## SNAKE CHANGED 1.1 SOHVA
        ## INDENTATION  CHANGED

##    if newloc in snake:
##        #If we hit the snake, the game is over
##        game_on = False
##        for item in snake:
##            sGrid[item[0]][item[1]].configure(bg = "red")
##            if len(snake) - 4 > highscore:
##                scores = open("snake_high_score.txt","w")
##                scores.write(str(len(snake)-4))
##                scores.close()
    for i in range (len(foodlist)):
        if newloc == foodlist[i]:
##        #If we hit food, the snake won't get shorter and the location of food is changed
            nextloc = newloc[0]-direction[0],newloc[1]-direction[1]
            while nextloc not in walls:
                newloc = nextloc
                nextloc = newloc[0]-direction[0],newloc[1]-direction[1]
             
        sGrid[snake[0]][snake[1]].configure(image = grass)
             #addFood() could be kept for fun to make the game more complicated
##        levellabel.configure(text = "Level: " + str(len(snake)-4))
##        if len(snake) - 4 > highscore:
##            scorelabel.configure(text = "Record: " + str(len(snake)-4))

    
    sGrid[snake[0]][snake[1]].configure(image = grass)
    snake = newloc
    ##LINE COMMENTED OUT 1.1 SOHVA
            
    ##sGrid[loc[0]][loc[1]].configure(image = snakeskin)
    #Make the head to point to the right direction
    nextloc = (newloc[0] + direction[0], newloc[1] + direction[1])
    if direction == (0,-1):
        if nextloc == food:
            snakehead = snakelefteat
        else:
            snakehead = snakeleft
    elif direction == (0,1):
        if nextloc == food:
            snakehead = snakerighteat
        else:
            snakehead = snakeright
    elif direction == (-1,0):
        if nextloc == food:
            snakehead = snakeupeat
        else:
            snakehead = snakeup
    else:
        if nextloc == food:
            snakehead = snakedowneat
        else:
            snakehead = snakedown
    sGrid[newloc[0]][newloc[1]].configure(image = snakehead)


#Functions to turn the snake
#If the snake is already moving to the same or opposite direction, nothing happens
##Version 1.2 SOHVA ADDED MOVES VARIABLE FOR DECIDING WHETHER PLAYER MOVES OR NOT
##Version 1.22 SOHVA FIXED A BUG WITH THE SNAKE MOVEMENT
def turnRight():
    global direction
    global new_direction
    global moves
    global movesOnce
##    if direction[0] != 0:
##        new_direction = (0,1)
    new_direction = (0,1)
    moves = True
    movesOnce = True
    

def turnLeft():
    global direction
    global new_direction
    global moves
    global movesOnce
##    if direction[0] != 0:
##        new_direction = (0,-1)
    new_direction = (0,-1)
    moves = True
    movesOnce = True

def turnUp():
    global direction
    global new_direction
    global moves
    global movesOnce
##    if direction[1] != 0:
##        new_direction = (-1,0)
    new_direction = (-1,0)
    moves = True
    movesOnce = True

def turnDown():
    global direction
    global new_direction
    global moves
    global movesOnce
##    if direction[1] != 0:
##        new_direction = (1,0)
    new_direction = (1,0)
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
    walls = wallcreator.createWalls(level)
    for wall in walls:
        sGrid[wall[0]][wall[1]].configure(image = grave)

def levelUp():
    global otherFinished
    otherFinished=False
    global walls
    global monsters
    global level
    global snake
    for row in sGrid:
        for square in row:
            square.configure(image = grass)
    snake = (1,1)
    level += 1
    levellabel.configure(text = "Level: " + str(level))
    monsters = monstercreator.createMonsters(level)
    createWalls(level)
    foodlist = []
    addFood()
    nextButton.configure(state="disabled")
    pause()
    
        
columns = 15
rows = 10
game_on = True
snake = []
highscore = 0
foodlist=[]
finish=(rows-3, columns-3)
walls = []


#Create the grid 
sGrid = []
for rownum in range(rows):
    row = []
    for colnum in range(columns):
        label = Tkinter.Label(top, image = grass, bg = "#6d6764", bd=0)
        #label = Tkinter.Label(top, bitmap="gray12", bg = "#e8e8e8")
        row += [label]
        label.grid(row = rownum+1, column = colnum)
    sGrid += [row]


monsters = monstercreator.createMonsters(1)
createSnake()

##1.6 SOHVA adds the variable for level
level = 1

levellabel = Tkinter.Label(top, text = "Level: " + str(level))
levellabel.grid(row = 0,columnspan=5,column  = 0)

createWalls(1)

#Place the food
food = (0,0)
addFood()


#Tells how to change coordinates
#up = (1,0); down = (-1,0); left = (0,-1); right = (0,1)
direction = (0,-1) #Left
new_direction = (0,-1)

## VERSION 1.2 SOHVA a boolean for the player movement
moves = False
movesOnce = False

otherFinished=False

quitButton = Tkinter.Button(top,text="Quit",command=top.destroy)
quitButton.grid(row = 0, column = columns + 1,rowspan=2)
newButton = Tkinter.Button(top,text="New Game", command = newGame)
newButton.grid(row=1,column=columns+1,rowspan=2)
nextButton = Tkinter.Button(top,text="Next Level", command = levelUp, state="disabled")
nextButton.grid(row=2,column=columns+1,rowspan=2)

#Bind the keys
#top.bind( "<KeyPress-Down>", turnDown)
#top.bind( "<KeyPress-s>", turnDown)
#top.bind( "<KeyPress-Up>", turnUp)
#top.bind( "<KeyPress-w>", turnUp)
#top.bind( "<KeyPress-Left>", turnLeft)
#top.bind( "<KeyPress-a>", turnLeft)
#top.bind( "<KeyPress-Right>", turnRight)
#top.bind( "<KeyPress-d>", turnRight)
#top.bind( "<space>", pause)

##Key releases VERSION 1.2 SOHVA
#top.bind( "<KeyRelease-Down>", stop)
#top.bind( "<KeyRelease-s>", stop)
#top.bind( "<KeyRelease-Up>", stop)
#top.bind( "<KeyRelease-w>", stop)
#top.bind( "<KeyRelease-Left>", stop)
#top.bind( "<KeyRelease-a>", stop)
#top.bind( "<KeyRelease-Right>", stop)
#top.bind( "<KeyRelease-d>", stop)

#Keeps track on the level

while True:
    if game_on:
        game()
    for i in range(10):
        time.sleep(0.3/10)
        top.update_idletasks()
        top.update()
    direction = new_direction
