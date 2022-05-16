def main(N, M, data):
    result = 0

    D = [
        ((0, 0), (1, 0), (0, 0), (0, 0)),
        ((0, 0), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, 0), (0, 0)),
        ((0, 1), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, -1), (-1, 0))
    ]

    for r in data:
        for c in r:
            print(c, end=" ")
            if 0 < c < 6:
                print(D[c-1])

        print()

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, data) )
