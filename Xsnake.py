##Version 1.1 Sohva

import Tkinter
import time
import random
import ImageTk

top = Tkinter.Tk()

#Initialize images
grass = ImageTk.PhotoImage(file = "grass.png")
foodimage = ImageTk.PhotoImage(file = "food.png")
snakeskin = ImageTk.PhotoImage(file = "snake.png")
snakeleft = ImageTk.PhotoImage(file = "snakeleft.png")
snakeup = ImageTk.PhotoImage(file = "snakeup.png")
snakeright = ImageTk.PhotoImage(file = "snakeright.png")
snakedown = ImageTk.PhotoImage(file = "snakedown.png")
snakelefteat = ImageTk.PhotoImage(file = "snakelefteat.png")
snakeupeat = ImageTk.PhotoImage(file = "snakeupeat.png")
snakerighteat = ImageTk.PhotoImage(file = "snakerighteat.png")
snakedowneat = ImageTk.PhotoImage(file = "snakedowneat.png")

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
    snake = (4,6)

def newGame():
    global snake
    global sGrid
    global food
    global columns
    global rows
    global game_on
    global direction
    global new_direction
    get_score()
    for row in sGrid:
        for item in row:
            item.configure(image = grass, bg = "green")
    createSnake()
    addFood()
    game_on = True
    direction = (0,-1)
    new_direction = (0,-1)
    levellabel.configure(text = "Level: " + str(len(snake)-4))
    
def addFood():
    global snake
    global sGrid
    global food
    global columns
    global rows
    while True:
        #Choses a random location
        chosen = (random.randint(0,rows-1),random.randint(0,columns-1))
        #Checks that it's not in the snake
        if chosen not in snake:
            food = chosen
            sGrid[food[0]][food[1]].configure(image = foodimage)
            break
    
def game():
    #Makes the snake move
    global snake
    global direction
    global game_on
    global highscore
    ## SNAKE CHANGED 1.1 S
    loc = snake
    #Update the location
    newloc = ((loc[0]+direction[0])%rows,(loc[1]+direction[1])%columns)

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
def turnRight(event):
    global direction
    global new_direction
    if direction[0] != 0:
        new_direction = (0,1)
    

def turnLeft(event):
    global direction
    global new_direction
    if direction[0] != 0:
        new_direction = (0,-1)

def turnUp(event):
    global direction
    global new_direction
    if direction[1] != 0:
        new_direction = (-1,0)

def turnDown(event):
    global direction
    global new_direction
    if direction[1] != 0:
        new_direction = (1,0)

def pause(even):
    global game_on
    game_on = not game_on
        
columns = 15
rows = 10
game_on = True
snake = []
highscore = 0

#Create the grid 
sGrid = []
for rownum in range(rows):
    row = []
    for colnum in range(columns):
        label = Tkinter.Label(top, image = grass, bg = "green")
        #label = Tkinter.Label(top, bitmap="gray12", bg = "#e8e8e8")
        row += [label]
        label.grid(row = rownum+1, column = colnum)
    sGrid += [row]


createSnake()
get_score()

scorelabel = Tkinter.Label(top, text = "Record: " + str(highscore))
scorelabel.grid(row = 0,columnspan=5,column  = 5)
levellabel = Tkinter.Label(top, text = "Level: " + str(len(snake)-4))
levellabel.grid(row = 0,columnspan=5,column  = 0)

#Place the food
food = (0,0)
addFood()

#Tells how to change coordinates
#up = (1,0); down = (-1,0); left = (0,-1); right = (0,1)
direction = (0,-1) #Left
new_direction = (0,-1)

quitButton = Tkinter.Button(top,text="Quit",command=top.destroy)
quitButton.grid(row = 0, column = columns + 1,rowspan=2)
newButton = Tkinter.Button(top,text="New Game", command = newGame)
newButton.grid(row=1,column=columns+1,rowspan=2)

#Bind the keys
top.bind( "<KeyPress-Down>", turnDown)
top.bind( "<KeyPress-s>", turnDown)
top.bind( "<KeyPress-Up>", turnUp)
top.bind( "<KeyPress-w>", turnUp)
top.bind( "<KeyPress-Left>", turnLeft)
top.bind( "<KeyPress-a>", turnLeft)
top.bind( "<KeyPress-Right>", turnRight)
top.bind( "<KeyPress-d>", turnRight)
top.bind( "<space>", pause)

while True:
    if game_on:
        game()
    for i in range(10):
        time.sleep(0.3/10)
        top.update_idletasks()
        top.update()
    direction = new_direction

for item in snake:
    sGrid[item[0]][item[1]].configure(bg="red")
