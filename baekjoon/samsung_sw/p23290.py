def main(M, S, data, Sx, Sy):
    result = 0
    print(M, S, data, Sx, Sy)

    return result

if __name__ == "__main__":
    M, S = tuple(map(int, input().split(" ")))
    data = [list(map(int, input().split(" "))) for _ in range(M)]
    Sx, Sy = tuple(map(int, input().split(" ")))

    print( main(M, S, data, Sx, Sy) )
