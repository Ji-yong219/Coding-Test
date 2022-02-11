def printBoard(N, M, nyx):
    for yy in range(N):
        for xx in range(M):
            if (yy, xx) in nyx:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()

def main(N, M, paper):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dx = [1, -1, 1, -1]
    dy = [0, 0, 0, 0]
    result = 0


    a = [(0, 0), (0, 1), (0, 2), (0, 3)]
    b = [(0, 0), (0, 1), (1, 0), (1, 1)]
    c = [(0, 0), (1, 0), (2, 0), (2, 1)]
    d = [(0, 0), (1, 0), (2, 0), (2, -1)]
    e = [(0, 0), (1, 0), (2, 0), (0, 1)]
    f = [(0, 0), (1, 0), (2, 0), (0, -1)]
    g = [(0, 0), (1, 0), (1, 1), (2, 1)]
    h = [(0, 0), (1, 0), (1, -1), (2, -1)]
    i = [(0, 0), (0, 1), (0, 2), (1, 1)]
    j = [(0, 0), (0, 1), (0, 2), (-1, 1)]

    for y in range(N):
        for x in range(M):
            for t in [a, b, c, d, e, f, g, h, i, j]:
                for k in range(4):
                    try:
                        cnt = 0
                        temp = []
                        for tt in t:
                            nx, ny = dx[k], dy[k]
                            if k>1:
                                yy, xx = y+tt[1]+ny, x+tt[0]*nx
                            else:
                                yy, xx = y+tt[0]+ny, x+tt[1]*nx

                            if (0 <= (yy) < N ) and (0 <= (xx) < M):
                                cnt += paper[yy][xx]
                                temp.append((yy, xx))
                            else:
                                break

                        # else:
                        #     print(k, temp)
                        #     printBoard(N, M, temp)
                        #     print("-"*30)

                        if cnt > result:
                            result = cnt
                    except IndexError:
                        continue

    return result

if __name__ == "__main__":
    N, M = tuple( map(int, input().split(" ") ) )
    paper = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, paper) )