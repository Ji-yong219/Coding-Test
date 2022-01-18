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

    result = []
    visited = set()

    x, y, R, B, O, new_R, new_B = [None for _ in range(7)]

    for i in range(N):
        if R and B and O:
            break
        
        for j in range(M):
            if map[i][j] == "R":
                R = (j, i)

            elif map[i][j] == "B":
                B = (j, i)

            elif map[i][j] == "O":
                O = (j, i)

            if R and B and O:
                break

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

        if (new_R, new_B) in visited or cnt>10:
            continue

        print(x, y, R, B, cnt)
        print()

        if new_R == O and new_R != new_B:
            result.append(cnt)
            continue

        map[R[1]][R[0]] = "."
        map[B[1]][B[0]] = "."

        map[new_R[1]][new_R[0]] = "R"
        map[new_B[1]][new_B[0]] = "B"

        map[O[1]][O[0]] = "O"

        R, B = new_R, new_B

        for i in range(4):
            if (dx[i], dy[i], R, B) not in dq:
                if isPossible(map, R, B, dx[i], dy[i]):
                    dq.append( (dx[i], dy[i], R, B, cnt+1) )

        visited.add( data[:2] )

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

    return R, B, O

N, M = map(int, input().split(" "))
data = [list(input()) for _ in range(N)]
print(main(N, M, data))