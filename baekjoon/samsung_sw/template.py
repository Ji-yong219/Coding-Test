from collections import deque
from copy import deepcopy

debug = False
debug2 = False


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def mirrored(array_2d):
    list_of_tuples = map(reversed, array_2d)
    return [list(elem) for elem in list_of_tuples]
    
def main(N, data):
    dq = deque()
    dx = [range(N), range(N-1, -1, -1), range(N), range(N-1, -1, -1)]
    dy = [range(N), range(N), range(N), range(N)]
    direction = ["←", "→", "↑", "↓"]
    direction = ["←", "↓", "→", "↑"]
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
            if debug:
                print("-"*30)
                print(f"count : {count+1}")

            for i in range(4):
                temp = (tuple(map(tuple, board)), i)
                if temp in visited:
                    continue

                visited.add((temp, i))
                # temp = move(deepcopy(board), dx[i], dy[i], i>1)
                temp = move2(N, deepcopy(board), i)
                dq.append( (temp, count+1) )

                if debug:
                    print("")
                    for j in range(N):
                        for k in range(N):
                            if board[j][k] == 0 :
                                print(f"{'.':^4}", end=" ")
                            else:
                                print(f"{board[j][k]:^4}", end=" ")

                        print(f" {direction[i]}  ", end="")

                        for k in range(N):
                            if temp[j][k] == 0 :
                                print(f"{'.':^4}", end=" ")
                            else:
                                print(f"{temp[j][k]:^4}", end=" ")
                        print()

    return max_data

def move(board, x, y, is_vertical):
    for ii in y:
        target = None

        for jj in x:
            if is_vertical:
                i, j = jj, ii

            else:
                i, j = ii, jj

            if target and board[i][j] != 0:
                if board[target[0]][target[1]] == board[i][j]:
                    board[target[0]][target[1]] *= 2
                    board[i][j] = 0

                target = None

            if target is None:
                target = (i, j)


        target = None
        for jj in x:
            if is_vertical:
                i, j = jj, ii

            else:
                i, j = ii, jj

            if target and board[i][j] != 0:
                board[target[0]][target[1]] = board[i][j]
                board[i][j] = 0
                target = None

            if target is None and board[i][j] == 0:
                target = (i, j)
    return board

def move2(N, board, d):
    if d == 1:
        board = rotated(board)
    elif d == 2:
        board = mirrored(board)
    elif d == 3:
        # board = mirrored(rotated(board))
        for i in range(3):
            board = rotated(board)

    if debug2:
        print("\n\n")
        for j in range(N):
            for k in range(N):
                if board[j][k] == 0 :
                    print(f"{'.':^4}", end=" ")
                else:
                    print(f"{board[j][k]:^4}", end=" ")
            print()

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

    if debug2:
        print("")
        for j in range(N):
            for k in range(N):
                if board[j][k] == 0 :
                    print(f"{'.':^4}", end=" ")
                else:
                    print(f"{board[j][k]:^4}", end=" ")
            print()

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