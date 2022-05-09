import sys

input =__import__('sys').stdin.readline

n = int(input())

ans = 0

while n >= 3 :
    if n % 5 == 0 :
        ans += n // 5
        n = 0
        break
    else :
        n -= 3
        ans += 1
if n > 0 :
    print(-1)
else :
    print(ans)
