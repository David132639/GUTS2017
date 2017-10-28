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
        walls = []
        for i in range(10):
            walls += [(i,0)]
            walls += [(i,14)]
        for j in range(1,14):
            walls += [(0,j)]
            walls += [(9,j)]
        for i in range(5):
            walls += [(i,5)]
            walls += [(i+4,9)]
    elif case == 2:
        for i in range(1,10):
            walls += [(3,i)]
        for i in range(3,11):
            if i != 8:
                walls += [(6,i)]
        for i in range(11,14):
            walls += [(5,i)]
    elif case == 3:
        for i in range(1,6):
            walls += [(i,4)]
        for i in range(2,9):
            walls += [(i,7)]
        for i in range(4,9):
            for j in range(9,11):
                walls += [(i,j)]
        walls += [(4,11),(5,11)]
    return walls
        
        
        
