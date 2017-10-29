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

