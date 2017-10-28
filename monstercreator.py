##Gives a list of obstacles given by the case number
##VERSION 1.1 SOHVA fixed a bug with the test case

import monster

def createMonsters(case):
    monsters = []
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
