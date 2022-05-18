color = ['black', 'brown', 'red', 'orange', 'yellow',
         'green', 'blue', 'violet', 'grey', 'white']

c1 = input()
c2 = input()
c3 = input()

n1 = color.index(c1)
n2 = color.index(c2)
n3 = color.index(c3)

ans = str(n1) + str(n2)

for i in range(n3):
    ans += '0'

ans = int(ans)

print(ans)