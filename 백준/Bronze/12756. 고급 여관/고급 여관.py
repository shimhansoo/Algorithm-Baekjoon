import sys

input =__import__('sys').stdin.readline

aa,ab = map(int, input().split())
ba,bb = map(int, input().split())

x = 0
y = 0

while True :
    bb -= aa
    ab -= ba
    if bb <= 0 :
        if ab > 0 :
            print("PLAYER A")
            break
        elif ab <= 0 :
            print("DRAW")
            break
    if ab <= 0 :
        if bb > 0 :
            print("PLAYER B")
            break
        elif bb <= 0 :
            print("DRAW")
            break