def main(gears, K, turns):
    result = 0

    return result

if __name__ == "__main__":
    gears = [list(map(int, list(input()))) for _ in range(4)]
    K = int(input())
    turns = [tuple(map(int, input().split(" "))) for _ in range(K)]

    print( main(gears, K, turns) )
