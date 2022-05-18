from sys import stdin

N = int(stdin.readline().strip())
F = int(stdin.readline().strip())

tmp = (N//100) * 100

while True:
    if(tmp % F == 0):
        ans = tmp
        break
    tmp += 1

ans = str(ans)
print(ans[-2:])