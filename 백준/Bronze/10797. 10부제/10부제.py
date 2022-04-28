N = int(input())
X = 0
car = list(map(int, input().split()))

for i in range(0,5):
    if(car[i] == N):
        X += 1
print(X)