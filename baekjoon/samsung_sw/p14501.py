from collections import deque

def main(N, plan):
    result = 0
    visited = []

    for n_day, (T, P) in enumerate(plan, 1):
        if n_day + T > N+1:
            break
        dq = deque([n_day-1])

        while dq:
            i = dq[-1] + plan[dq[-1]][0]

            while i < N:
                if i + plan[i][0] > N:
                    i += 1
                    continue

                temp = tuple(dq)

                if temp+(i,) not in visited:
                    dq.append(i)
                    i += plan[i][0]
                    continue
                i += 1

            visited.append(tuple(dq))

            result = max(result, sum([plan[ii][1] for ii in dq]))

            i = dq.pop()


    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, plan) )
