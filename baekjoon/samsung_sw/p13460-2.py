from collections import deque

def printBoard(data):
    for row in data:
        for c in row:
            print(f"{c:3}", end="")
        print("\n")
    print()

def isPossible(map, R, B, dx, dy):
    x1, y1 = R
    x2, y2 = B
    
    nx1, ny1 = x1 + dx, y1 + dy
    nx2, ny2 = x2 + dx, y2 + dy

    # print(f"({dx}, {dy})\t{nx1}, {ny1}\t{nx2}, {ny2}", end="\t->\t")
        
    if map[ny1][nx1] in [".", "O"] or map[ny2][nx2] in [".", "O"]:
        # print("true")
        return True

    # print("false")
    return False

def main(r, C, map):
    global N
    global M

    N, M = r, C

    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = None, None

    result = []

    visited = set()

    # printBoard(map)

    R, B, O, new_R, new_B = [None for _ in range(5)]

    # finding R & B
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

    visited.add((R, B))

    for i in range(4):
        # data = isPossible(map, R, B, O, visited, dx[i], dy[i], last)
        # map2 = [_[:] for _ in map]
        # data = incline(map2, dx[i], dy[i], R, B, O)
        # if data and data[:2] not in visited:
        if isPossible(map, R, B, dx[i], dy[i]):
            dq.append( (dx[i], dy[i], R, B, 1) )

    print(dq)
    printBoard(map)
    print("="*50)

    while dq:
        print(f"\n\nbefore deque :")
        for dd in dq:
            print(dd)
        # last = x, y
        x, y, R, B, cnt = dq.popleft()
        print(f"\npop\nxy : ({x}, {y})\tR : {R}, B : {B}")

        if new_R:
            map[new_R[1]][new_R[0]] = "."
            map[new_B[1]][new_B[0]] = "."

            map[R[1]][R[0]] = "R"
            map[B[1]][B[0]] = "B"

            map[O[1]][O[0]] = "O"

        print("\n\nbefore")
        printBoard(map)

        data = incline(map, N, M, x, y, R, B, O)
        print(f"data : {data}")

        new_R, new_B = data[:2]

        print(data[:2], visited)
        if (new_R, new_B) in visited:
            continue



        map[R[1]][R[0]] = "."
        map[B[1]][B[0]] = "."

        map[new_R[1]][new_R[0]] = "R"
        map[new_B[1]][new_B[0]] = "B"

        map[O[1]][O[0]] = "O"

        R, B = new_R, new_B

        print("\nafter")
        print(R, B, new_R, new_B)
        printBoard(map)
        print("\n")

        if new_R == O and new_R != new_B:
            result.append(cnt)

        for i in range(4):
            print()
            print(dx[i], dy[i], (x,y))

            if data and data[:2] not in visited:
                if (dx[i], dy[i], R, B) not in dq:
                    if isPossible(map, R, B, dx[i], dy[i]):
                        dq.append( (dx[i], dy[i], R, B, cnt+1) )


        visited.add( data[:2] )
        print(f"\nafter deque :")
        for dd in dq:
            print(dd)
        print("\n\n")


    print(f"result : {result}")
    result = min(result) if result!=[] else -1
    result = -1 if result > 10 else result

    return result

def incline(map, N, M, dx, dy, R, B, O):
    iter1, iter2 = None, None

    v = False

    next_goal = None

    drc = None
    if dy == -1:
        iter1 = range(N)
        iter2 = range(M)
        v = True
        drc = "↑"
    elif dy == 1:
        iter1 = range(N-1, -1, -1)
        iter2 = range(M)
        v = True
        drc = "↓"
    elif dx == -1:
        iter1 = range(N)
        iter2 = range(M)
        drc = "←"
    elif dx == 1:
        iter1 = range(N)
        iter2 = range(M-1, -1, -1)
        drc = "→"

    print(drc, "before", R, B, end="\t")

    if v:
        iter1, iter2 = iter2, iter1

    for i in iter1:
        l, c, prv, now, goal = [None for _ in range(5)]

        for j in iter2:
            l = c
            c = (i, j) if v else (j, i)

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

            if R == B == O:
                return R, B, O

            # printBoard(map)
                
        # print("\n\n")
        # break

    print("after", R, B)
    return R, B, O

if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    data = [list(input()) for _ in range(N)]
    print( main(N, M, data) )