import sys

input = __import__('sys').stdin.readline

a = int(input())
x = 0
while(x != a) :
    N,M = map(int,input().split())
    print((M*2-N),M-(M*2-N))
    x += 1