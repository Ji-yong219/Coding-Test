def main(N, M, data):
    result = 0

    print(N, M, data)

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, M, data) )
