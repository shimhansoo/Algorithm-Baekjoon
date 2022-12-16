import sys

input = __import__('sys').stdin.readline

N, M = map(int,input().split())

if ( M <= 2 ) :
    print("NEWBIE!")
elif ( M > 2 ) :
    if(N < M) :
        print("TLE!")
    elif(N >= M) :
        print("OLDBIE!")