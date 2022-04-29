dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

ddy = [(-1, 0, 1), (-1, 0, 1), (-1, -1, -1), (1, 1, 1)]
ddx = [(1, 1, 1), (-1, -1, -1), (-1, 0, 1), (-1, 0, 1)]

def is_wall(walls, y1, x1, y2, x2, d):
    dfy = y2 - y1
    dfx = x2 - x1

    if abs(dfy) > 1 or abs(dfx) > 1:
        return True


    case = 0
    if abs(dfy) > 0 and abs(dfx) > 0:
        case = 5

    elif dfy == 0:
        if dfx > 0:
            case = 1
        else:
            case = 2
    else:
        if dfy > 0:
            case = 3
        else:
            case = 4

    # print(y1, x1, y2, x2, case)
    for w in walls:
        if case == 1:
            if y1 == w[0]-1 and x1 == w[1]-1 and w[2] == 1:
                return True

        elif case == 2:
            if y2 == w[0]-1 and x2 == w[1]-1 and w[2] == 1:
                return True

        elif case == 3:
            if y2 == w[0]-1 and x2 == w[1]-1 and w[2] == 0:
                return True

        elif case == 4:
            if y1 == w[0]-1 and x1 == w[1]-1 and w[2] == 0:
                return True

        elif case == 5:
            minx = min(x1, x2)
            maxy = max(y1, y2)

            if d == 1:
                if (minx == w[1]-1 and  maxy == w[0]-1 and w[2] == 0)\
                        or (maxy-1 == w[0]-1 and minx == w[1]-1 and w[2] == 1):
                    return True

                if (minx == w[1]-1 and  maxy-1 == w[0]-1 and w[2] == 0)\
                        or (maxy == w[0]-1 and minx == w[1]-1 and w[2] == 1):
                    return True

            elif d == 2:
                if (minx+1 == w[1]-1 and maxy == w[0]-1 and w[2] == 0)\
                        or (maxy-1 == w[0]-1 and minx == w[1]-1 and w[2] == 1):
                    return True

                if (minx+1 == w[1]-1 and maxy == w[0]-1 and w[2] == 0)\
                        or (maxy == w[0]-1 and minx == w[1]-1 and w[2] == 1):
                    return True

            elif d == 3:
                if (minx == w[1]-1 and maxy == w[0]-1 and w[2] == 1)\
                        or (maxy == w[0]-1 and minx+1 == w[1]-1 and w[2] == 0):
                    return True

                if (minx == w[1]-1 and maxy == w[0]-1 and w[2] == 1)\
                        or (maxy == w[0]-1 and minx == w[1]-1 and w[2] == 0):
                    return True

            elif d == 4:
                if (minx == w[1] and maxy-0 == w[0]-1 and w[2] == 1)\
                        or (maxy == w[0]-1 and minx+1 == w[1]-1 and w[2] == 0):
                    return True

                if (minx == w[1]-1 and maxy-1 == w[0]-1 and w[2] == 1)\
                        or (maxy == w[0]-1 and minx == w[1]-1 and w[2] == 0):
                    return True



            # if minx == w[1] and w[2] == 1:
            #     return True
            # if maxy == w[0] and w[2] == 0:
            #     return True

    return False

def wind(data, ws, walls, R, C):
    for y, x, d in ws:
        ny = y + dy[d-1]
        nx = x + dx[d-1]

        qs = set()
        new_wind(5, data, d, ny, nx, walls, R, C, qs)

        for s in list(qs):
            data[s[0]][s[1]] += s[2]

def new_wind(p, data, d, y, x, walls, R, C, qs):
    if p == 0:
        return

    qs.add((y, x, p))
    l = [
        (y+(ddy[d-1][0]), x+(ddx[d-1][0])),
        (y+(ddy[d-1][1]), x+(ddx[d-1][1])),
        (y+(ddy[d-1][2]), x+(ddx[d-1][2]))
    ]

    for i, (ny, nx) in enumerate(l):
        if 0 <= ny < R and 0 <= nx < C:
            if not is_wall(walls, y, x, ny, nx, d):
                new_wind(p-1, data, d, ny, nx, walls, R, C, qs)
            continue
            if i == 1:
                if not is_wall(walls, y, x, ny, nx):
                    new_wind(p-1, data, d, ny, nx, walls, R, C, qs)

            elif i == 0:
                if d == 1 or d == 2:
                    if not(is_wall(walls, y-1, x, l[0][1], l[0][1]) or \
                            is_wall(walls, y, x, y-1, x)):
                        new_wind(p-1, data, d, ny, nx, walls, R, C, qs)

                elif d == 3 or d == 4:
                    if not (is_wall(walls, y, x-1, l[0][0], l[0][1]) or \
                            is_wall(walls, y, x, y, x-1)):
                        new_wind(p-1, data, d, ny, nx, walls, R, C, qs)

            elif i == 2:
                if d == 1 or d == 2:
                    if not (is_wall(walls, y, x, y+1, x) or \
                            is_wall(walls, y+1, x, l[2][0], l[2][1])):
                        new_wind(p-1, data, d, ny, nx, walls, R, C, qs)

                elif d == 3 or d == 4:
                    if not (is_wall(walls, y, x, y, x+1) or \
                            is_wall(walls, y, x+1, l[2][0], l[2][1])):
                        new_wind(p-1, data, d, ny, nx, walls, R, C, qs)

def control_temp(R, C, data, walls):
    data2 = [i[:] for i in data]

    for y in range(R):
        for x in range(C):
            for i in range(1, 5, 2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C:
                    if not is_wall(walls, y, x, ny, nx, i):
                        dif = abs(data2[y][x] - data2[ny][nx])//4
                        if dif > 0:
                            if data2[y][x] > data2[ny][nx]:
                                data[y][x] -= dif
                                data[ny][nx] += dif
                            else:
                                data[y][x] += dif
                                data[ny][nx] -= dif

def reduce_outer_temp(data, R, C):
    for x in range(C):
        data[0][x] = 0 if data[0][x] < 1 else data[0][x]-1
        data[R-1][x] = 0 if data[R-1][x] < 1 else data[R-1][x]-1

    for y in range(1, R-1):
        data[y][0] = 0 if data[y][0] < 1 else data[y][0]-1
        data[y][C-1] = 0 if data[y][C-1] < 1 else data[y][C-1]-1

def check(data, K, ts):
    for t in ts:
        if data[t[0]][t[1]] < K:
            return False
    return True

def main(R, C, K, data, walls):
    result = 0
    ws = []
    ts = []
    for y in range(R):
        for x in range(C):
            d = data[y][x]
            if d == 5:
                ts.append((y, x))
                data[y][x] = 0
            elif 0 < d < 5:
                ws.append((y, x, d))
                data[y][x] = 0

    while True:
        wind(data, ws, walls, R, C)
        # for d in data:
        #     print(d)
        # break
        control_temp(R, C, data, walls)
        reduce_outer_temp(data, R, C)
        result += 1
        if check(data, K, ts):
            break

    result = 101 if result > 100 else result
    return result

if __name__ == "__main__":
    R, C, K = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(R)]
    walls = [list(map(int, input().split(" "))) for _ in range(int(input()))]

    print( main(R, C, K, data, walls) )
