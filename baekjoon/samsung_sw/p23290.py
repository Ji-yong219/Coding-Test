sdy = (-1, 0, 1, 0)
sdx = (0, -1, 0, 1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)

ar = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
sr = ["↑", "←", "↓", "→"]
debug = False

def print_grid(grid, smells, sy, sx):
    mx = 0
    for r in grid:
        for e in r:
            mx = max(mx, len(e))

    mx = max(4, mx)
    print(f"{' ' * (mx // 2) * 4}Grid{' ' * (mx // 2) * 4}\t\t{' ' * 5}냄새{' ' * 5}\t\t{' ' * 5}상어{' ' * 5}")
    print(f"""┌{"┬".join(["─" * (mx)] * 4)}┐""", end="\t")
    print(f"""┌{"┬".join(["─" * (3)] * 4)}┐""", end="\t")
    print(f"""┌{"┬".join(["─" * (3)] * 4)}┐""", end="")
    for i, r in enumerate(grid):
        print("\n│", end="")
        smell = []
        shark = []
        for j, e in enumerate(r):
            print(f"{''.join([ar[a - 1] for a in e]):^{mx}s}", end="│")

            for sm in smells:
                if (i, j) == sm[:2]:
                    smell.append(f"{sm[2]:^3d}")
                    break
            else:
                smell.append(f"{' ':^3s}")

            if sy == i and sx == j:
                shark.append(f"{'S':^3s}")
            else:
                shark.append(f"{' ':^3s}")

        print(f"""\t│{"│".join(smell)}│""", end="")
        print(f"""\t│{"│".join(shark)}│""", end="")

        print(f"""\n├{"┼".join(["─" * (mx)] * 4)}┤""", end="\t")
        print(f"""├{"┼".join(["─" * (3)] * 4)}┤""", end="\t")
        print(f"""├{"┼".join(["─" * (3)] * 4)}┤""", end="")
    print(f"""\r└{"┴".join(["─" * (mx)] * 4)}┘""", end="\t")
    print(f"""└{"┴".join(["─" * (3)] * 4)}┘""", end="\t")
    print(f"""└{"┴".join(["─" * (3)] * 4)}┘""")
    print()

def move_fish(grid, copy, sy, sx, smells):
    for y in range(4):
        for x in range(4):
            if len(grid[y][x]) != []:
                for d in copy[y][x]:
                    if debug:
                        print(f"\n{y}, {x}의 {d} 하는 중")
                        print_grid(grid, smells, sy, sx)
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
                            if debug:
                                print(f"{ny}, {nx}는 가도 되는 곳 이니까 기존 {[ar[j - 1] for j in copy[ny][nx]]}에서")
                            d2 = (d - i) % 8
                            d2 = 8 if d2 == 0 else d2
                            grid[ny][nx].append(d2)
                            if debug:
                                print(f"{ar[d2 - 1]}를 추가해서 {[ar[j - 1] for j in grid[ny][nx]]}가 됐고")
                                print(f"기존 {[ar[j - 1] for j in copy[y][x]]}는 {ar[d - 1]}를 빼서")
                                print(grid[y][x], y, x, d)

                            grid[y][x].remove(d)
                            if debug:
                                print(grid[y][x], y, x, d)
                                print(f"{grid[y][x]}가 된다\n\n")
                            break
                    if y == 2 and x == 2:
                        print_grid(grid, smells, sy, sx)

    return grid

def find_routes(cnt, grid, sy, sx, route, routes, kill):
    grid = [[gg[:] for gg in g] for g in grid]
    psb = []
    for i in range(4):
        ny = sy + sdy[i]
        nx = sx + sdx[i]

        if 0 <= ny < 4 and 0 <= nx < 4:
            c = len(grid[ny][nx])
            psb.append((c, ny, nx, str(i + 1)))

    for e in psb:
        ny = e[1]
        nx = e[2]

        t = grid[ny][nx][:]
        if len(route) == 2:
            routes.append((kill + len(t), route + e[3]))
        else:
            grid[sy][sx].clear()
            find_routes(cnt + 1, grid, ny, nx, route + e[3], routes, kill + len(t))
            grid[sy][sx] = t[:]

    return routes

def move_shark(p, sy, sx, route, grid, smells):
    for r in route:
        r = int(r) - 1

        sy += sdy[r]
        sx += sdx[r]
        if len(grid[sy][sx]) > 0:
            grid[sy][sx] = []
            for i, sm in enumerate(smells):
                if sy == sm[0] and sx == sm[1]:
                    smells[i] = (sy, sx, p)
                    break
            else:
                smells.append((sy, sx, p))

    return sy, sx

def main(S, data, sy, sx):
    # 격자 초기화
    grid = [[[] for _ in range(4)] for _ in range(4)]
    for f in data:
        y = f[0] - 1
        x = f[1] - 1
        grid[y][x].append(f[2])

    smells = []

    for p in range(1, S + 1):
        if debug:
            print(f"{p}번째 연습 시작")
        # 현재 물고기 복제
        copy = [[[] for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                copy[i][j] = grid[i][j][:]

        # 물고기 이동
        if debug:
            print(f"물고기 이동 전 그리드")
            print_grid(grid, smells, sy, sx)

        grid = move_fish(grid, copy, sy, sx, smells)
        if debug:
            print(f"물고기 이동 후 그리드")
            print_grid(grid, smells, sy, sx)

        # 상어 경로 경우의 수 찾기
        routes = find_routes(0, grid, sy, sx, "", [], 0)

        routes.sort(key=lambda x: (-x[0], x[1]))
        if debug:
            print(f"경로 : {routes}")
            print_grid(grid, smells, sy, sx)

        # 상어 이동
        sy, sx = move_shark(p, sy, sx, routes[0][1], grid, smells)

        if debug:
            print(f"일케 이동합니다. {' '.join([sr[int(i) - 1] for i in routes[0][1]])}")

            print(f"상어 이동 후 그리드")
            print_grid(grid, smells, sy, sx)

        # 냄새 제거
        smells2 = [j[:] for j in smells]
        for i, sm in enumerate(smells2):
            if sm[2] + 2 <= p:
                smells.remove(smells2[i])
        if debug:
            print(f"냄새 제거 후 그리드 : {p}")
            print_grid(grid, smells, sy, sx)

        # 복제 완료
        for i in range(4):
            for j in range(4):
                grid[i][j].extend(copy[i][j])

        if debug:
            print(f"복제 후 그리드")
            print_grid(grid, smells, sy, sx)
            print(f"물고기 수 : {sum([sum(len(j) for j in i) for i in grid])}")
            print("=" * 80)

    # 물고기 수
    result = sum([sum(len(j) for j in i) for i in grid])
    return result


if __name__ == "__main__":
    M, S = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(M)]
    sy, sx = [int(i) - 1 for i in input().split(" ")]

    print(main(S, data, sy, sx))
