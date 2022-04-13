def main(N, M, data, y, x, d):
    result = 0
    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    r, c, d = tuple(map(int, input().split(" ")))
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, M, data, r, c, d) )
