import sys

input =__import__('sys').stdin.readline

a = int(input())

cute = int(0)
notCute = int(0)
for i in range(a) :
    b = int(input())
    if b == 0 :
        notCute += 1
    elif b == 1 :
        cute += 1
if cute > notCute :
    print("Junhee is cute!") 
elif cute < notCute :
    print("Junhee is not cute!")