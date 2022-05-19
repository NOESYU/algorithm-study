N = int(input())

name = list(input()) #각 비교를 위해 list로

patterns = name

for i in range(N-1):
    name2 = list(input()) 
    for j in range(len(name)):
        if(name[j] == name2[j]):
            pass
        else:
            patterns[j] = '?'

ans = ''.join(patterns)

print(ans)