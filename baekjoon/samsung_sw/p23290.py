def main(M, S, data, Sx, Sy):
    result = M

    grid = [[0]*4 for _ in range(4)]

    dy = (0, -1, -1, -1, 0, 1, 1, 1)
    dx = (-1, -1, 0, 1, 1, 1, 0, -1)

    sdy = (-1, 0, 1, 0)
    sdx = (0, -1, 0, 1)

    smells = []

    for cnt in range(1, S+1):
        # 냄새 제거
        for sm in smells:
            if sm[2] + 2 == cnt:
                del sm

        # 물고기 복제
        data2 = [i.copy() for i in data]

        # 물고기 이동
        for idx, (Fy, Fx, Fd) in enumerate(data):
            for i in range(8):
                ny = (Fy-1) + dy[Fd-1 %8]
                nx = (Fx-1) + dx[Fd-1 %8]

                if (0 <= ny < 4) and (0 <= nx < 4):
                    if ny != Sy-1 or nx != Sx-1:
                        for y, x, _ in smells:
                            if (y-1, x-1) == (ny, nx):
                                break
                        
                        else:
                            grid[Fy-1][Fx-1] -= 1
                            grid[ny][nx] += 1
                            data[idx] = [ny+1, nx+1, Fd]
                            break
                Fd -= 1

        # 상어 이동
        routes = []
        cnts = []
        print(f"zz1 : {Sy}, {Sx}")
        for d in range(4):
            ny = Sy + sdy[d]
            nx = Sx + sdx[d]

            if (0 <= ny < 4) and (0 <= nx < 4):
                cnts.append((d+1, grid[ny][nx], (ny, nx)))
            
        print(f"zz1 : {[r[0] for r in cnts if r[1] == max([t[1] for t in cnts])]}")
        for a in [r[0] for r in cnts if r[1] == max([t[1] for t in cnts])]:
            ny, nx = a[2]
            cnts2 = []
            for d2 in range(4):
                ny = Sy + sdy[d2]
                nx = Sx + sdx[d2]

                if (0 <= ny < 4) and (0 <= nx < 4):
                    cnts2.append((d2+1, grid[ny][nx], (ny, nx)))

            print(f"zz2: {[r[0] for r in cnts2 if r[1] == max([t[1] for t in cnts2])]}")
            for b in [r[0] for r in cnts2 if r[1] == max([t[1] for t in cnts2])]:
                ny, nx = a[2]
                cnts3 = []
                for d3 in range(4):
                    ny = Sy + sdy[d3]
                    nx = Sx + sdx[d3]

                    if (0 <= ny < 4) and (0 <= nx < 4):
                        cnts3.append((d3+1, grid[ny][nx], (ny, nx)))

                print(f"zz3 : {[r[0] for r in cnts3 if r[1] == max([t[1] for t in cnts3])]}")
                for c in [r[0] for r in cnts3 if r[1] == max([t[1] for t in cnts3])]:
                    ny, nx = a[2]
                    routes.append( f"{a[0]}{b[0]}{c[0]}" )

        routes.sort()
        print(f"route 총 개수는 {len(routes)}")
        print(routes)
        for r in routes:
            temp = (Sy, Sx)
            for d in r:
                d = int(d) - 1
                ny = Sy-1 + sdy[d]
                nx = Sx-1 + sdx[d]

                if not((0 <= ny < 4) and (0 <= nx < 4)):
                    Sy, Sx = temp
                    break

                if grid[ny][nx] != 0:
                    smells.append((ny+1, nx+1, cnt))

                    for i, f in enumerate(data):
                        if f[0]-1 == ny and f[1]-1 == nx:
                            del data[i]
                            Sy, Sx = temp
                            break

                    grid[ny][nx] = 0
                Sy, Sx = ny+1, nx+1
                print(f"상어 이동함 {Sy}, {Sx}")
            else:
                print("일케 이동했음", r)
                break
        
        # 복제 완료
        l = len(data)
        for i in range(len(data2)):
            d = data2[i]

            if d in data[:l]:
                continue

            grid[d[0]-1][d[1]-1] += 1
            data.append(d)

        print(f"마지막 상어 위치 : {Sy}, {Sx}")
    print(f"기존 물고기 : {data2}")
    print(f" 복제 완료 물고기 : {data}")
    print(f"냄새 : {smells}")
    result = len(data)

    return result

if __name__ == "__main__":
    M, S = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(M)]
    Sy, Sx = tuple(map(int, input().split(" ")))

    print( main(M, S, data, Sx, Sy) )
