def roll(dice, d):
    hor = [(1, 0), (1, 1), (1, 2), (3, 1)]
    ver = [(0, 1), (1, 1), (2, 1), (3, 1)]
    a, b, c = 3, 0, -1

    if d in [3, 4]:
        hor = ver
    if d in [2, 3]:
        a, b, c = 0, 3, 1

    temp = dice[ hor[a][0] ][ hor[a][1] ]
    for i in range(a, b, c):
        dice[ hor[i][0] ][ hor[i][1] ] = dice[ hor[i+c][0] ][ hor[i+c][1] ]
    dice[ hor[b][0] ][ hor[b][1] ] = temp

    return dice
    
def main(N, M, x, y, data, command):
    dice = [ [0, 0, 0] for _ in range(4) ]

    for d in command:
        backup = (x, y)

        if d == 1:
            x += 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y -= 1
        elif d == 4:
            y += 1

        if not ((-1 < y < N) and (-1 < x < M)):
            x, y = backup
            continue

        dice = roll(dice, d)
            
        if data[y][x] == 0:
            data[y][x] = dice[3][1]

        elif data[y][x] != 0:
            dice[3][1], data[y][x] = data[y][x], 0

        print(dice[1][1])

if __name__ == "__main__":
    N, M, y, x, K = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(N)]
    command = tuple(map(int, input().split(" ")))

    main(N, M, x, y, data, command)