##Gives a list of obstacles given by the case number
##VERSION 1.1 SOHVA fixed a bug with the test case
##Version 1.2 Marija added a boss monster to be in the list by default

import monster

def createMonsters(case):
    monsters = [monster.Monster((8,13), [(8, 13), (8, 12), (8, 11), (7,11), (6, 11), (6, 12), (6, 13), (7,13)])]
    ##Testcase
    if case == 1:
        monsters += [monster.Monster((3,1),[(3,1),(3,2),(2,2),(2,1)])]
        monsters += [monster.Monster((7,1),[(7,1),(7,2),(6,2),(6,1)])]
        return monsters
    elif case == 2:
        monsters += [monster.Monster((3,1),[(3,1),(3,2),(2,2),(2,1)])]
        monsters += [monster.Monster((7,1),[(7,1),(7,2),(6,2),(6,1)])]
        monsters += [monster.Monster((7,5),[(7,5),(7,4)])]
        return monsters
