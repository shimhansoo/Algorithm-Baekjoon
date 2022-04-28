import sys

input =__import__('sys').stdin.readline

M = int(input())
D = int(input())
if M == 2 :
    if D > 18 :
        print("After")
    elif D < 18 :
        print("Before")
    elif D == 18 :
        print("Special")
elif M != 2 :
    if M < 2 :
        print("Before")
    elif M > 2 :
        print("After")