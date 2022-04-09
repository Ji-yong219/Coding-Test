def main(N, plan):
    result = 0
    
    cost = [0] * (N+1)

    for i in range(N-1, -1, -1):
        d = i + plan[i][0]
        if d < N:
            cost[i] = max(cost[i+1], cost[d] + plan[i][1])
        else:
            cost[i] = cost[i+1]

    result = max(cost)
    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ tuple(map(int, input().split(" "))) for _ in range(N) ]
    print( main(N, plan) )
