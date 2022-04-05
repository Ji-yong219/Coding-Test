def main(N, plan):
    result = 0
    
    cost = [0] * (N+1)

    for i in range(N+1):
        for j in range(0, i):
            cost[i] = max(cost[i], cost[j])

            if i == j + plan[j][0]:
                cost[i] = max(cost[i], cost[j] + plan[j][1])

    result = max(cost)
    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ tuple(map(int, input().split(" "))) for _ in range(N) ]
    print( main(N, plan) )
