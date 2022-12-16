import sys

input = __import__('sys').stdin.readline

t = int(input())
for i in range(t) :
    n = int(input())
    PointA = 0
    PointB = 0
    for j in range(n) :
        PlayerA,PlayerB = map(str,input().split())
        if (PlayerA == "R") :
            if(PlayerB == "R") :
                PointA += 1
                PointB += 1
            elif(PlayerB == "S") :
                PointA += 1
            elif(PlayerB == "P") :
                PointB += 1
        elif (PlayerA == "S") :
            if(PlayerB == "S") :
                PointA += 1
                PointB += 1
            elif(PlayerB == "P") :
                PointA += 1
            elif(PlayerB == "R") :
                PointB += 1
        elif (PlayerA == "P") :
            if(PlayerB == "P") :
                PointA += 1
                PointB += 1
            elif(PlayerB == "R") :
                PointA += 1
            elif(PlayerB == "S") :
                PointB += 1
    if(PointA > PointB) :
        print("Player 1")
    elif(PointA < PointB) :
        print("Player 2")
    elif(PointA == PointB) :
        print("TIE")