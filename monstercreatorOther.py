##Gives a list of obstacles given by the case number
##VERSION 1.1 SOHVA fixed a bug with the test case
##Version 1.2 Marija added a boss monster to be in the list by default

import monster

def createMonsters(case):
    monsters = [monster.Monster((8,13), [(8, 13), (8, 12), (8, 11), (7,11), (6, 11), (6, 12), (6, 13), (7,13)])]

    if case == 1:
        monsters += [monster.Monster((1,2),[(1,2),(1,3),(1,4),(1,5),(1,6),\
                                            (1,7),(1,8),(1,9),(1,10),(1,11),\
                                            (1,12),(1,13),(2,13),(3,13),(4,13),\
                                            (4,12),(4,11),(4,10),(3,10),(2,10),\
                                            (1,10),(1,9),(1,8),(1,7),(1,6),(1,5),\
                                            (1,4),(1,3)])]
        monsters += [monster.Monster((5,1),[(5,1),(5,2),(5,3),(5,3),(5,2)])]

    elif case == 2:
        monsters += [monster.Monster((7,7),[(7,7),(8,7)])]
        monsters += [monster.Monster((7,9),[(7,9),(8,9)])]
        monsters += [monster.Monster((3,11),[(3,11),(3,12),(3,13),(3,12)])]
        route = []
        for i in range(2,9):
            route += [(i,1)]
            route += [(i,1)]
        for i in range(1,6):
            route += [(8,i)]
            route += [(8,i)]
        for i in [7,6,5,4,3,2,1]:
            route += [(i,5)]
            route += [(i,5)]
        for i in range(1,8):
            route += [(i,4)]
            route += [(i,4)]
        for i in [3,2]:
            route += [(7,i)]
            route += [(7,i)]
        for i in [7,6,5,4,3,2]:
            route += [(i,2)]
            route += [(i,2)]
        for i in [2,1]:
            route += [(1,i)]
        monsters += [monster.Monster((2,2),route)]
    elif case == 3:
        monsters += [monster.Monster((3,1),[(3,1),(3,2),(4,2),(4,1)])]
        monsters += [monster.Monster((2,5),[(2,5),(2,6)])]
        monsters += [monster.Monster((2,10),[(2,10),(2,11),(2,12),(2,11)])]
        monsters += [monster.Monster((1,13),[(1,13),(2,13),(3,13),(2,13)])]
        i = 8
        monsters += [monster.Monster((5,i),[(5,i),(5,1),(6,i),(7,i),(8,i),(8,i),(7,i),(6,i)])]
        i = 9
        monsters += [monster.Monster((8,i),[(8,i),(8,i),(7,i),(6,i),(5,i),(5,i),(6,i),(7,i)])]
        route = []
        for i in range(2,10):
            route += [(1,i)]
        route += [(1,9)]
        for i in [10,9,8,7,5,4,3,2,1]:
            route += [(1,i)]
        monsters += [monster.Monster((1,2),route)]
    return monsters
