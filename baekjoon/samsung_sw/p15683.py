def main(N, M, data):
    result = 0

    DC = (4, 2, 4, 4, 1)

    D = [
        ((0, 0), (1, 0), (0, 0), (0, 0)),

        ((0, 0), (1, 0), (0, 0), (-1, 0)),

        ((0, 1), (1, 0), (0, 0), (0, 0)),

        ((0, 1), (1, 0), (0, 0), (-1, 0)),

        ((0, 1), (1, 0), (0, -1), (-1, 0))
    ]




    for r in data:
        print(r)
    print("")

    cams = []

    for y in range(N):
        for x in range(M):
            c = data[y][x]

            if c != "#" and 0 < c < 6:
                cams.append((y, x, data[y][x]-1))

    CS = [[j for j in range(DC[i[2]])] for i in cams]
    print(f"CS : {CS}")


                # for i in range(4):
                #     ny = y + D[c-1][i][0]
                #     nx = x + D[c-1][i][1]

                    # while 0 <= ny < N and 0 <= nx < M and data[ny][nx] != 6:
                    #     if data[ny][nx] == 0:
                    #         data[ny][nx] = "#"
                    #
                    #     ny = ny + D[c-1][i][0]
                    #     nx = nx + D[c-1][i][1]

    for r in data:
        print(r)

    print(f"cams : {cams}")

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, data) )
