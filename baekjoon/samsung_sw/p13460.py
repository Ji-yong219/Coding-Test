from collections import deque

def isPossible(map, R, B, dx, dy):
    (x1, y1), (x2, y2) = R, B
    
    nx1, ny1 = x1+dx, y1+dy
    nx2, ny2 = x2+dx, y2+dy

    if map[ny1][nx1] in [".", "O"] or map[ny2][nx2] in [".", "O"]:
        return True

    return False

def main(N, M, map):
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    result = []
    visited = set()

    R, B, O = [None for _ in range(3)]

    for i in range(N):
        if R and B and O:
            break
        
        for j in range(M):
            if map[i][j] == "R":
                R = (j, i)
                map[i][j] = "."

            elif map[i][j] == "B":
                B = (j, i)
                map[i][j] = "."

            elif map[i][j] == "O":
                O = (j, i)

            if R and B and O:
                break

    dq.append((R, B, 0))

    while dq:
        R1, B1, cnt = dq.popleft()

        if R1 == O and R1 != B1:
            result.append(cnt)
            continue

        if cnt >= 10:
            continue

        for i in range(4):
            if isPossible(map, R1, B1, dx[i], dy[i]):
                R2, B2 = incline(map, N, M, dx[i], dy[i], R1, B1, O)

                if  (R2, B2) not in visited:
                    dq.append( (R2, B2, cnt+1) )
                    visited.add( (R2, B2) )

    result = min(result) if result else -1
    return -1 if result > 10 else result

def incline(map, N, M, dx, dy, R, B, O):
    iter1, iter2, next_goal = [None for _ in range(3)]

    if dy == -1:
        iter2 = range(N)
        iter1 = range(M)
    elif dy == 1:
        iter2 = range(N-1, -1, -1)
        iter1 = range(M)
    elif dx == -1:
        iter1 = range(N)
        iter2 = range(M)
    elif dx == 1:
        iter1 = range(N)
        iter2 = range(M-1, -1, -1)

    for i in iter1:
        l, c, prv, now, goal = [None for _ in range(5)]

        for j in iter2:
            l = c
            c = (i, j) if dy else (j, i)

            if l:
                prv = map[l[1]][l[0]]
            now = map[c[1]][c[0]]

            if l == goal and now in ["."]:
                next_goal = c

            if (prv == "#" or l in [R, B]) and now in ["."] and c not in [R, B]:
                goal = c

            if now == "O":
                goal = c

            elif c == R and goal and prv != "#" and l not in [R, B]:
                R = goal

                if goal == O:
                    next_goal = O

                goal = next_goal

            elif c == B and goal and prv != "#" and l not in [R, B]:
                B = goal

                if goal == O:
                    next_goal = O

                goal = next_goal

    return R, B

N, M = map(int, input().split(" "))
data = [list(input()) for _ in range(N)]
print(main(N, M, data))