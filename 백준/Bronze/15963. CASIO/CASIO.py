import sys

input =__import__('sys').stdin.readline

a,b = map(int, input().split())

if a == b:
    print("1")
elif a != b :
    print("0")