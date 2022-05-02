import sys

input =__import__('sys').stdin.readline

a = int(input())
i = 0

while i != a :
    b,c = map(int, input().split(','))
    print(b+c)
    i+=1