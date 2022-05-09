N = int(input())

for i in range(N):
    a,b = map(int, input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(a//b,a%b))