import sys

input =__import__('sys').stdin.readline

a = int(input())

for i in range(9) :
    print("{} * {} = {}".format(a,i+1,(i+1)*a))