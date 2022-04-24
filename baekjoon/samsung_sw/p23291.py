def check(data, K):
    return max(data) - min(data) <= K

def main(N, K, data):
    result = 0

    grid = [[0] * N for _ in range(N-1)]
    grid.append(data.copy())

    while True:
        mx = max(data)
        mn = min(data)

        # Exit Condition
        if mx - mn <= K:
            break
        else:
            result += 1

        # Step 1 Start
        while True:
            try:
                idx = data.index(mn)
                data[idx] = mn+1
            except:
               break
        # Step 1 End


        # Step 2 Start
        y = N-1
        x = 0
        grid[y][x], grid[y-1][x+1] = 0, grid[y][x]
        while True:
            try:
                xs = 0
                xe = 0
                ys = -1

                # Find X index higher than 2F
                for i in range(N):
                    if xs == 0 and grid[N-2][i] != 0:
                        xs = i
                    if xs != 0 and grid[N-2][i] == 0:
                        xe = i
                        break

                # Find Y index higher than 2F
                for i in range(N):
                    if grid[i][xs] != 0:
                        ys = i
                        break

                if xe+N-ys+1 >= N:
                    break

                for xb, ya in zip(range(xs, xe), range(N-(xe-xs)-1, N-1)):
                    for yb, xa in zip(range(N-1, ys-1, -1), range(xe, xe+N-ys+2)):
                        grid[ya][xa], grid[yb][xb] = grid[yb][xb], 0
                        

            except:
                break

        break
        # Step 2 End


        # Step 3 Start

        # Step 3 End


        # Step 4 Start

        # Step 4 End
    
    for r in grid:
        print(r)

    return result

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    data = list(map(int, input().split(" ")))

    print( main(N, K, data) )

