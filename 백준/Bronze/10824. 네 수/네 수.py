import sys

input =__import__('sys').stdin.readline

a,b,c,d = map(int,input().split())
ab = str(a) + str(b)
cd = str(c) + str(d)
result = int(ab) + int(cd)
print(result)

