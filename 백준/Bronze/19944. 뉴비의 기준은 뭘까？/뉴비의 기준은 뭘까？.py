import sys

input =__import__('sys').stdin.readline

a,b = map(int, input().split())

if b <= 2 :
    print("NEWBIE!")
elif b > 2 :
    if a >= b :
        print("OLDBIE!")
    elif a < b :
        print("TLE!")
