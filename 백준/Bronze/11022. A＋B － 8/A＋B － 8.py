import sys

input =__import__('sys').stdin.readline

a = int(input())

for i in range(a) :
    x,y = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1,x,y,x+y))