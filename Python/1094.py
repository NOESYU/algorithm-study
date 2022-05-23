def BinaryFunc(X, list):
    a = X // 2
    b = X % 2
    list.append(b)

    if a == 0:
        return list
    else:
        return BinaryFunc(a, list)

binumber = []
X = int(input())

binumber = BinaryFunc(X, binumber)

print(binumber.count(1))