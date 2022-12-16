import sys

input = __import__('sys').stdin.readline

a = int(input())

plug = 1

for i in range(a) :
    x = int(input())
    plug += (x - 1)
print(plug)