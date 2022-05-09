rifle = 350.34
eye = 230.90
ear = 190.55
arm = 125.30
leg = 180.90

N = int(input())
for i in range(N):
    a,b,c,d,e = map(int,input().split())
    print("${0:.2f}".format(a*rifle + eye*b + ear*c + arm*d + leg*e))