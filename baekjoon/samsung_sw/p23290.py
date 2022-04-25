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
        for idx, (Fx, Fy, Fd) in enumerate(data):
            for _ in range(8):
                ny = (Fy-1) + dy[Fd-1 %8]
                nx = (Fx-1) + dx[Fd-1 %8]

                if (0 <= ny < 4) and (0 <= nx <= 4):
                    if ny != Sy-1 and nx != Sx:
                        for y, x, _ in smells:
                            if (y, x) == (ny, nx):
                                break
                        
                        else:
                            grid[Fy-1][Fx-1] -= 1
                            grid[ny][nx] += 1
                            data[idx] = [nx+1, ny+1, Fd]
                            break

                Fd -= 1

        # 상어 이동
        suc = False
        temp = Sy, Sx
        routes = []

        cnts = [10e4] * 4
        for d in range(4):
            ny = Sy + sdy[d]
            nx = Sx + sdx[d]

            if (0 <= ny < 4) and (0 <= nx < 4):
                cnts[d] = grid[ny][nx]
            
            
        temp = Sy, Sx
        for a in [d for d in range(4) if cnts[d] == min(cnts)]:
            cnts2 = [10e4] * 4
            for d in range(4):
                ny = Sy + sdy[d]
                nx = Sx + sdx[d]

                if (0 <= ny < 4) and (0 <= nx < 4):
                    cnts2[d] = grid[ny][nx]

            temp2 = Sy, Sx
            for b in [d for d in range(4) if cnts2[d] == min(cnts2)]:
                cnts3 = [10e4] * 4
                for d in range(4):
                    ny = Sy + sdy[d]
                    nx = Sx + sdx[d]

                    if (0 <= ny < 4) and (0 <= nx < 4):
                        cnts3[d] = grid[ny][nx]
            
                temp3 = Sy, Sx            
                for c in [d for d in range(4) if cnts3[d] == min(cnts3)]:
                    routes.append( f"{(a+1)}{b+1}{c+1}" )

                Sy, Sx = temp3
            Sy, Sx = temp2
        Sy, Sx = temp

        routes.sort()
        for d in list(routes[0]):
            d = int(d)-1

            ny = Sy + sdy[d]
            nx = Sx + sdx[d]

            grid[ny][nx] = 0
            smells.append((ny, nx, cnt))


        # for i in range(4):
        #     for j in range(4):
        #         for k in range(4):
        #             for l in (i, j, k):

        #                 ny = sdy[l]
        #                 nx = sdx[l]

        # 복제 만들기
        print(data)
        print(data2)

    result = len(data)

    return result

if __name__ == "__main__":
    M, S = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(M)]
    Sx, Sy = tuple(map(int, input().split(" ")))

    print( main(M, S, data, Sx, Sy) )
