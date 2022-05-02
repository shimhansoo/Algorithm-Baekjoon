import sys

input =__import__('sys').stdin.readline

s,k,h = map(int,input().split())

if s + k + h >= 100 :
    print("OK")
elif s + k + h < 100 :
    if s > k :
        if k > h :
            print("Hanyang") # S K H
        elif k < h :
            print("Korea") # S H K 
    elif s < k :
        if s < h :
            print("Soongsil") # K H S
        elif s > h :
            print("Hanyang") # K S H
    elif s < h :
        if s < k :
            print("Soongsil") # H K S
        elif s > k :
            print("Korea") # H S K
