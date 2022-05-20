board = []

for i in range(8):
    board.append(list(input()))

white = 0

for i in range(8):
    for j in range(8):
        if ((i + j) % 2 == 0):
            if board[i][j] == 'F':
                white += 1

print(white)