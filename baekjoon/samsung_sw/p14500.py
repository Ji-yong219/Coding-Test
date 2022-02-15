import sys

def main(N, M, paper):
    result = 0

    TET = (
        ((0, 1), (0, 2), (0, 3)),
        ((1, 0), (2, 0), (3, 0)),
        ((0, 1), (1, 0), (1, 1)),

        ((1, 0), (2, 0), (2, 1)),
        ((1, 0), (2, 0), (2, -1)),
        ((1, 0), (2, 0), (0, 1)),
        ((1, 0), (2, 0), (0, -1)),

        ((0, 1), (0, 2), (1, 2)),
        ((0, -1), (0, -2), (1, -2)),
        ((0, 1), (0, 2), (-1, 2)),
        ((0, -1), (0, -2), (-1, -2)),

        ((1, 0), (1, 1), (2, 1)),
        ((1, 0), (1, -1), (2, -1)),
        ((0, 1), (1, 1), (1, 2)),
        ((0, -1), (1, -1), (1, -2)),

        ((0, 1), (0, 2), (1, 1)),
        ((0, 1), (0, 2), (-1, 1)),

        ((1, 0), (2, 0), (1, 1)),
        ((1, 0), (2, 0), (1, -1)),
    )

    for y in range(N):
        for x in range(M):
            for t in TET:
                s = paper[y][x]
                for tt in t:
                    yy, xx = y+tt[1], x+tt[0]

                    if (0 <= (yy) < N ) and (0 <= (xx) < M):
                        s += paper[yy][xx]
                    else:
                        break

                result = max(s, result)

    return result

if __name__ == "__main__":
    N, M = tuple( map(int, sys.stdin.readline().split(" ") ) )
    paper = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

    print( main(N, M, paper) )
