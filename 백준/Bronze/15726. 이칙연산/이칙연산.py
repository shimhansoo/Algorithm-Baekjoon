import sys

input =__import__('sys').stdin.readline

A,B,C = map(int, input().split())

x = A * B / C
y = A / B * C
if x >= y :
    print(int(x))
elif x < y :
    print(int(y))

