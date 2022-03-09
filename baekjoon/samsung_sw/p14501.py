def main(N, plan):
    result = 0

    t_day = 1
    for n_day, (T, P) in enumerate(plan, 1):
        if n_day + T > N+1:
            break
        pay = P
        t_day = n_day + T

        while t_day <= N:
            temp = t_day + plan[t_day-1][0]
            if temp > N+1:
                break
            else:
                pay += plan[t_day-1][1]
                t_day = temp

        print(f"{pay}")

        result = max(result, pay)
    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, plan) )
