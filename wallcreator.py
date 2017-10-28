def createWalls(case):
    #Testcase, creates walls around a 10x15
    if case == 1:
        walls = []
        for i in range(10):
            walls += [(i,0)]
            walls += [(i,14)]
        for j in range(1,14):
            walls += [(0,j)]
            walls += [(9,j)]
        return walls
    elif case == 2:
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
        return walls