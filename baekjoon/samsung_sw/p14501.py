from collections import deque

def main(N, plan):
    result = 0
    visited = ()

    dq = deque( [0] )
    while dq: 
        i = dq[-1] + plan[dq[-1]][0]
        sm = plan[dq[-1]][1]
    
        while i < N:
            if i + plan[i][0] > N:
                i += 1
                continue

            temp = tuple(dq)

            if temp + (i, ) not in visited:
                dq.append(i)
                sm += plan[i][1]
                i += plan[i][0]
                continue

            i += 1

        visited += (tuple(dq), )
        result = max(result, sm)
        dq.pop()

    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ tuple(map(int, input().split(" "))) for _ in range(N) ]
    print( main(N, plan) )
