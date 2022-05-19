N = int(input())

divisor = list(map(int, input().split()))

min = divisor[0]
max = divisor[0]

for x in divisor:
    if (min > x):
        min = x
    if (max < x):
        max = x

print(min*max)