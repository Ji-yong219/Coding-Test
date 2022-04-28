sdy = (-1, 0, 1, 0)
sdx = (0, -1, 0, 1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)

def move_fish(grid, copy, sy, sx, smells):
    for y in range(4):
        for x in range(4):
            if len(grid[y][x]) != "":
                for d in copy[y][x]:
                    d = int(d)
                    for i in range(8):
                        ny = y + dy[(d - 1 - i) % 8]
                        nx = x + dx[(d - 1 - i) % 8]
                        ok = True

                        if not (0 <= ny < 4 and 0 <= nx < 4) \
                                or (ny == sy and nx == sx):
                            ok = False

                        for s in smells:
                            if s[0] == ny and s[1] == nx:
                                ok = False

                        if ok:
                            d2 = (d - i) % 8
                            d2 = 8 if d2 == 0 else d2
                            grid[ny][nx] += str(d2)
                            grid[y][x] = grid[y][x].replace(str(d), "", 1)
                            break

    return grid

def find_routes(grid, sy, sx, route, routes):
    for i in range(4):
        ny = sy + sdy[i]
        nx = sx + sdx[i]

        if 0 <= ny < 4 and 0 <= nx < 4:
            if len(route) == 2:
                routes.append((route + str(i+1)))

            else:
                find_routes(grid, ny, nx, route + str(i+1), routes)
    return routes

def find_max_route(grid, sy, sx, routes):
    route = ""
    mx = 0

    for r in routes:
        ny, nx = sy, sx
        k = 0
        temp = []
        for d in r:
            d = int(d)-1
            ny += sdy[d]
            nx += sdx[d]

            if 0 <= ny < 4 and 0 <= nx < 4:
                k += len(grid[ny][nx])

                if grid[ny][nx] != "":
                    temp.append((ny, nx, grid[ny][nx]))
                    grid[ny][nx] = ""
            else:
                break
        else:
            if k > mx:
                route = r
                mx = k
            elif route == "":
                route = r

        for t in temp:
            grid[t[0]][t[1]] = t[2]

    return route

def move_shark(p, sy, sx, route, grid, smells):
    for r in route:
        r = int(r) - 1

        sy += sdy[r]
        sx += sdx[r]
        if grid[sy][sx] != "":
            grid[sy][sx] = ""
            for i, sm in enumerate(smells):
                if sy == sm[0] and sx == sm[1]:
                    smells[i] = (sy, sx, p)
                    break
            else:
                smells.append((sy, sx, p))

    return sy, sx

def main(S, data, sy, sx):
    # 격자 초기화
    grid = [["" for _ in range(4)] for _ in range(4)]
    for f in data:
        y = f[0] - 1
        x = f[1] - 1
        grid[y][x] += str(f[2])

    smells = []

    for p in range(1, S + 1):
        # 현재 물고기 복제
        copy = [g[:] for g in grid]

        # 물고기 이동
        grid = move_fish(grid, copy, sy, sx, smells)

        # 상어 경로 경우의 수 찾기
        routes = find_routes(grid, sy, sx, "", [])
        route = find_max_route(grid, sy, sx, routes)

        # 상어 이동
        sy, sx = move_shark(p, sy, sx, route, grid, smells)

        # 냄새 제거
        smells2 = [j[:] for j in smells]
        for i, sm in enumerate(smells2):
            if sm[2] + 2 <= p:
                smells.remove(smells2[i])

        # 복제 완료
        for i in range(4):
            for j in range(4):
                grid[i][j] += copy[i][j]
        
    # 물고기 수
    result = sum([sum(len(j) for j in i) for i in grid])
    return result

if __name__ == "__main__":
    M, S = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(M)]
    sy, sx = [int(i) - 1 for i in input().split(" ")]

    print(main(S, data, sy, sx))
