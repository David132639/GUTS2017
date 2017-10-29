def createWalls(case):
    walls = []
    #Barriers
    for i in range(10):
        walls += [(i,0)]
        walls += [(i,14)]
    for j in range(1,14):
        walls += [(0,j)]
        walls += [(9,j)]

    #Cases
    if case == 1:
        for i in range(10):
            walls += [(2,i)]
            walls += [(5,i+4)]
    elif case == 2:
        for i in range(1,6):
            walls += [(i,3)]
        for i in range(3,7):
            for j in range(6,11):
                walls += [(i,j)]
    elif case == 3:
        walls += [(2,4),(2,7),(2,8),(2,9)]
        walls += [(6,5),(7,5),(8,5)]
        for i in range(3,14):
            walls += [(4,i)]
        for i in range(6,9):
            for j in range(1,3):
                walls += [(i,j)]
    return walls
        
        
        
