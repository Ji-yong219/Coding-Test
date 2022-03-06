def main(plan):
    result = 0

    for day, (T, P) in enumerate(plan, 1):
        print(day, T, P)

    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(plan) )
