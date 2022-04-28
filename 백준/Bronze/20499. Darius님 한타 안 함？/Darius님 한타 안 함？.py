import sys

input =__import__('sys').stdin.readline

K,D,A = map(int, input().split('/'))

if D == 0 :
    print("hasu")
elif D != 0 :
    if K + A < D :
        print("hasu")
    elif K + A >= D :
        print("gosu")