import sys

input = __import__('sys').stdin.readline

a = int(input())
cute = 0

for i in range(a) :
    x = int(input())
    if(x == 1) :
        cute += 1
    elif(x == 0) :
        cute -= 1
if cute > 0 :
    print("Junhee is cute!")
elif cute < 0 :
    print("Junhee is not cute!")

    