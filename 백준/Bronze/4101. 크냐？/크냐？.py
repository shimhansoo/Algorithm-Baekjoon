import sys

input =__import__('sys').stdin.readline

while True :
    a,b = map(int, input().split())
    
    if a == 0 and b == 0 :
        break

    if a <= b :
        print("No")
    elif a > b :
        print("Yes")
