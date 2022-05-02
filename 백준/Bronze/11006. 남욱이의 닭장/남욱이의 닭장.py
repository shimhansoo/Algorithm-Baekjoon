import sys

input =__import__('sys').stdin.readline

a = int(input())
i = 0

while int(i) != a :
    b,c = map(int, input().split())
    print((c*2 -b),(c -(c*2 -b) ) )
    i+=1