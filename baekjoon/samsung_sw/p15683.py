def main(N, M, data):
    result = 0

    D = [
        ((0, 0), (1, 0), (0, 0), (0, 0)),
        ((0, 0), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, 0), (0, 0)),
        ((0, 1), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, -1), (-1, 0))
    ]

    for y in range(N):
        for x in range(M):
            c = data[y][x]

            if 0 < c < 6:
                for i in range(4):
                    ny = y + D[c-1][i][0]
                    nx = x + D[c-1][i][1]

                    print(data[ny][nx])
        print()

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, data) )
