from collections import deque

def isPossible(map, R, B, dx, dy):
    x1, y1 = R
    x2, y2 = B
    
    nx1, ny1 = x1 + dx, y1 + dy
    nx2, ny2 = x2 + dx, y2 + dy

    if map[ny1][nx1] in [".", "O"] or map[ny2][nx2] in [".", "O"]:
        return True

    return False

def main(N, M, map):
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = None, None

    result = []

    visited = set()

    R, B, O, new_R, new_B = [None for _ in range(5)]

    for i in range(N):
        if R and B and O:
            break
        
        for j in range(M):
            if R and B and O:
                break

            if map[i][j] == "R":
                R = (j, i)

            elif map[i][j] == "B":
                B = (j, i)

            elif map[i][j] == "O":
                O = (j, i)

    visited.add((R, B))

    for i in range(4):
        if isPossible(map, R, B, dx[i], dy[i]):
            dq.append( (dx[i], dy[i], R, B, 1) )

    while dq:
        x, y, R, B, cnt = dq.popleft()

        if new_R:
            map[new_R[1]][new_R[0]] = "."
            map[new_B[1]][new_B[0]] = "."

            map[R[1]][R[0]] = "R"
            map[B[1]][B[0]] = "B"

            map[O[1]][O[0]] = "O"

        data = incline(map, N, M, x, y, R, B, O)

        new_R, new_B = data[:2]

        if (new_R, new_B) in visited:
            continue

        map[R[1]][R[0]] = "."
        map[B[1]][B[0]] = "."

        map[new_R[1]][new_R[0]] = "R"
        map[new_B[1]][new_B[0]] = "B"

        map[O[1]][O[0]] = "O"

        R, B = new_R, new_B

        if new_R == O and new_R != new_B:
            result.append(cnt)

        for i in range(4):
            if (dx[i], dy[i], R, B) not in dq:
                dq.append( (dx[i], dy[i], R, B, cnt+1) )

        visited.add( data[:2] )

    result = min(result) if result!=[] else -1
    result = -1 if result > 10 else result

    return result

def incline(map, N, M, dx, dy, R, B, O):
    iter1, iter2 = None, None

    h, v = False, False

    next_goal = None

    R2, B2 = R, B

    drc = None
    if dy == -1:
        iter1 = range(0, N)
        iter2 = range(0, M)
        v = True
        drc = "↑"
    elif dy == 1:
        iter1 = range(N-1, -1, -1)
        iter2 = range(0, M-1)
        v = True
        drc = "↓"
    elif dx == -1:
        iter1 = range(0, N)
        iter2 = range(0, M)
        h = True
        drc = "←"
    elif dx == 1:
        iter1 = range(0, N)
        iter2 = range(M-1, -1, -1)
        h = True
        drc = "→"

    if v:
        iter1, iter2 = iter2, iter1

    for i in iter1:
        l, c = None, None
        prv, now = None, None

        goal = None

        for j in iter2:
            l = c

            if v:
                c = (i, j)
            else:
                c = (j, i)

            if l:
                prv = map[l[1]][l[0]]
            now = map[c[1]][c[0]]

            if l == goal and now in ["."]:
                next_goal = c

            if prv in ["#", "R", "B"] and now in ["."]:
                goal = c

            if now == "O":
                goal = c

            elif now == "R" and goal and prv in [".", "O"]:
                R = goal
                map[goal[1]][goal[0]] = now
                map[c[1]][c[0]] = "."

                if goal == O:
                    map[goal[1]][goal[0]] = "O"
                    next_goal = O

                goal = next_goal

            elif now == "B" and goal and prv in [".", "O"]:
                B = goal
                map[goal[1]][goal[0]] = now
                map[c[1]][c[0]] = "."

                if goal == O:
                    map[goal[1]][goal[0]] = "O"
                    next_goal = O

                goal = next_goal

    map[R[1]][R[0]] = "."
    map[B[1]][B[0]] = "."

    map[R2[1]][R2[0]] = "R"
    map[B2[1]][B2[0]] = "B"

    map[O[1]][O[0]] = "O"

    return R, B, O

N, M = map(int, input().split(" "))
data = [list(input()) for _ in range(N)]
print(main(N, M, data))