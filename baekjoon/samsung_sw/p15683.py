from this import d


def main(N, M, data):
    result = 0

    D = [
        ((0, 0), (1, 0), (0, 0), (0, 0)),
        ((0, 0), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, 0), (0, 0)),
        ((0, 1), (1, 0), (0, 0), (-1, 0)),
        ((0, 1), (1, 0), (0, -1), (-1, 0))
    ]

    print(N, M)
    print(data)

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, data) )
