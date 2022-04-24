def step3(grid, N):
    arr = []
    for x in range(N):
        for y in range(N-1, 0, -1):
            a = grid[y][x]
            b = grid[y][x-1]
            c = grid[y-1][x]

            if a == 0:
                continue

            if b != 0:
                d = abs(a-b)//5
                if d > 0:
                    if a > b:
                        arr.append(((y, x), (y, x-1), d))
                    else:
                        arr.append(((y, x-1), (y, x), d))

            if c != 0:
                d = abs(a-c)//5
                if d > 0:
                    if a > c:
                        arr.append(((y, x), (y-1, x), d))
                    else:
                        arr.append(((y-1, x), (y, x), d))

    for a, b, d in arr:
        grid[a[0]][a[1]] -= d
        grid[b[0]][b[1]] += d

def step4(grid, N):
    data = []
    for x in range(N):
        for y in range(N-1, -1, -1):
            v = grid[y][x]
            if v == 0:
                continue
            data.append(v)

    grid = [[0] * N for _ in range(N-1)]
    grid.append(data.copy())
    return grid, data

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

        result += 1

        # Step 1 Start
        while True:
            try:
                idx = grid[-1].index(mn)
                grid[-1][idx] = mn+1
            except:
               break
        # Step 1 End

        # Step 2 Start
        y = N-1
        x = 0
        grid[y][x], grid[y-1][x+1] = 0, grid[y][x]

        while True:
            xs = -1
            xe = -1
            ys = -1

            # Find X index higher than 2F
            for i in range(N):
                if xs == -1 and grid[N-2][i] != 0:
                    xs = i
                    xe = i + 1
                elif xs != -1 and grid[N-2][i] != 0:
                    xe = i + 1

            # Find Y index higher than 2F
            for i in range(N):
                if grid[i][xs] != 0:
                    ys = i
                    break

            if xe - ys > 0:
                break

            for xb, ya in zip(range(xs, xe), range(N-(xe-xs)-1, N-1)):
                for yb, xa in zip(range(N-1, ys-1, -1), range(xe, xe+N-ys+2)):
                    grid[ya][xa], grid[yb][xb] = grid[yb][xb], 0
                    
        # Step 2 End

        step3(grid, N)
        grid, data = step4(grid, N)

        # Step 5 Start
        c = N//2
        d = 1
        xs = c-1
        xe = -1
        ys = N-2
        ye = N-1
        for _ in range(2):
            for yb, ya in zip(range(N-1, N-d-1, -1), range(ys, ye)):
                for xb, xa in zip(range(xs, xe, -1), range(N-c, N)):
                    grid[ya][xa], grid[yb][xb] = grid[yb][xb], 0

            ye = ys
            ys -= d*2
            d *= 2

            xe = xs
            c //= 2
            xs += c

        # Step 5 End

        step3(grid, N)
        grid, data = step4(grid, N)

    return result

if __name__ == "__main__":
    N, K = tuple(map(int, input().split(" ")))
    data = list(map(int, input().split(" ")))

    print( main(N, K, data) )
