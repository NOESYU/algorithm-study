N = input()

cycle = 0
result = 0

if(len(N) < 2):
    N = '0' + N

tmp = N

while True:
    if (tmp == result):
        break

    sum = str(int(N[0]) + int(N[1]))
    result = N[-1] + sum[-1]

    N = result
    
    cycle += 1

print(cycle)