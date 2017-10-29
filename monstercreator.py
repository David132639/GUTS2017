##Gives a list of obstacles given by the case number
##VERSION 1.1 SOHVA fixed a bug with the test case
##Version 1.2 Marija added a boss monster to be in the list by default

import monster

def createMonsters(case):
    monsters = [monster.Monster((8,13), [(8, 13), (8, 12), (8, 11), (7,11), (6, 11), (6, 12), (6, 13), (7,13)])]
    print case
    if case == 1:
        monsters += [monster.Monster((3,1),[(3,1),(3,2),(2,2),(2,1)])]
        monsters += [monster.Monster((7,1),[(7,1),(7,2),(6,2),(6,1)])]
        monsters += [monster.Monster((7,5),[(7,5),(7,4)])]
    elif case == 2:
        monsters += [monster.Monster((2,10),[(2,10),(2,11),(2,12),(3,12),(3,11),(3,10)])]
        monsters += [monster.Monster((4,8),[(4,8),(5,8),(6,8),(7,8),(8,8),(7,8),(6,8),(5,8)])]
        route = []
        for i in range(1,14):
            route += [(4,i)]
        for i in [4,3,2,1]:
            route += [(i,13)]
        for i in range(13,0,-1):
            route += [(1,i)]
        routeCopy = route + []
        for i in reversed(routeCopy[:-1]):
            route+= [i]
        monsters += [monster.Monster((4,1),route)]
    elif case == 3:
        monsters += [monster.Monster((1,3),[(1,3),(2,3)])]
        monsters += [monster.Monster((3,1),[(3,1),(3,2),(3,3),(3,2)])]
        monsters += [monster.Monster((2,8),[(2,8),(2,9),(2,10),(2,11),(2,10),(2,9)])]
        monsters += [monster.Monster((4,12),[(4,12),(4,12),(4,13),(4,13)])]
        monsters += [monster.Monster((6,8),[(6,8),(6,9)])]
        monsters += [monster.Monster((2,1),[(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(8,1),\
                                            (7,1),(6,1),(5,1),(4,1),(3,1),(2,1),(1,1)])]
    return monsters
