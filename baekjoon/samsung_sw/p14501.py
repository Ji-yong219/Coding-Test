def main(plan):
    result = 0

    for p in plan:
        print(p)

    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(plan) )
