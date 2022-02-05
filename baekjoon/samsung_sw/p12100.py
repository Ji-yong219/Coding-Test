from collections import deque
from copy import deepcopy

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def mirrored(array_2d):
    list_of_tuples = map(reversed, array_2d)
    return [list(elem) for elem in list_of_tuples]
    
def main(N, data):
    dq = deque()
    visited = set()

    max_data = 0

    dq.append( (deepcopy(data), 0) )

    while dq:
        board, count = dq.popleft()

        for r in board:
            temp = max(r)
            if max_data < temp:
                max_data = temp

        if count < 5:
            for i in range(4):
                temp = (tuple(map(tuple, board)), i)
                if temp in visited:
                    continue

                visited.add((temp, i))
                temp = move(N, deepcopy(board), i)
                dq.append( (temp, count+1) )

    return max_data

def move(N, board, d):
    if d == 1:
        board = rotated(board)
    elif d == 2:
        board = mirrored(board)
    elif d == 3:
        for i in range(3):
            board = rotated(board)

    for i in range(N):
        t = 0

        for j in range(1, N):
            if board[i][t] == 0 and board[i][j] != 0:
                board[i][t] = board[i][j]
                board[i][j] = 0

            if board[i][t] != 0 and board[i][j] != 0:
                if board[i][t] == board[i][j]:
                    board[i][t] *= 2
                    board[i][j] = 0
                    
                elif t+1 != j:
                    board[i][t+1] = board[i][j]
                    board[i][j] = 0
                t += 1

    if d == 1:
        for i in range(3):
            board = rotated(board)
    elif d == 2:
        board = mirrored(board)
    elif d == 3:
        board = rotated(board)

    return board


if __name__ == "__main__":
    N = int( input() )
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, data) )