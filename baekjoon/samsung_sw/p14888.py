def main(N, data):
    result = 0
    print(N, data)
    return result

if __name__ == "__main__":
    N = int( input() )
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, data) )
