import sys

input =__import__('sys').stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180 :
    if(a ==b and b == c) :
        print("Equilateral")
    elif( a != b and b != c and c != a) :
        print("Scalene")
    elif( a==b and b != c) :
        print("Isosceles")
    elif( c==b and b != a) :
        print("Isosceles")
    elif( a==c and b != c) :
        print("Isosceles")
elif a + b + c != 180 :
    print("Error")