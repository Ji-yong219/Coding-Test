def main(R, C, K, data, W, wall):
    result = 0

    print(R, C, K, data, W, wall)

    return result

if __name__ == "__main__":
    R, C, K = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(R)]
    W = int(input())
    wall = [list(map(int, input().split(" "))) for _ in range(W)]

    print( main(R, C, K, data, W, wall) )
