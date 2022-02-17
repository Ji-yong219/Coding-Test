def main(N, plan):
    result = 0

    print(f"N : {N}\tplan : {plan}")

    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, plan) )
