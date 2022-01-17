from ast import Break
from collections import deque

def printBoard(data):
    for row in data:
        for c in row:
            print(f"{c:3}", end="")
        print("\n")
    print()

def isPossible(map, R, B, O, visited, dx, dy, last):
    x1, y1 = R
    x2, y2 = B
    
    nx1, ny1 = x1 + dx, y1 + dy
    nx2, ny2 = x2 + dx, y2 + dy
    print(dx, dy, last)
    # print(f"x1 : {x1}, y1 : {y1}\tx2 : {x2}, y2 : {y2}")
    # print(f"nx1 : {nx1}, ny1 : {ny1}\tnx2 : {nx2}, ny2 : {ny2}")
    # print(f'R:{data[ny1][nx1]}\tB:{data[ny2][nx2]}\n')
    if dx == last[0] or dy == last[1]:
        print("cut1\n\n")
        return False
        
    if map[ny1][nx1] in [".", "O"] or map[ny2][nx2] in [".", "O"]:
        (rx, ry), (bx, by), (ox, oy) = incline8(map, dx, dy, R, B, O)
        temp = ((nx1, ny1), (nx2, ny2))
        if temp not in visited:
            print(f"yeap\t:\t{((rx, ry), (bx, by), (ox, oy))}\n\n")
            return ((rx, ry), (bx, by), (ox, oy))
    
    print("cut2\n\n")
    return False


def main(r, C, board):
    global N
    global M
    global next_goal

    last = None
    map, N, M = board, r, C
    R, B, O = None, None, None

    result = []
    count = 1
    
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = None, None

    next_goal = None
    visited = set()

    printBoard(map)

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

    last = (9, 9)
                
    for i in range(4):
        data = isPossible(map, R, B, O, visited, dx[i], dy[i], last)
        if data is not None and data[:2] not in dq:
            dq.append((R, B))

    print(dq)
    printBoard(map)
    print("="*50)

    while dq:
        R2, B2 = dq.popleft()

        map[R[1]][R[0]] = "."
        map[B[1]][B[0]] = "."

        map[R2[1]][R2[0]] = "R"
        map[B2[1]][B2[0]] = "B"

        # print("special -----")

        # data = isPossible(map, R, B, O, visited, x, y, last)
        # if data is not None:
            # r = incline7(x, y)
            # R, B, O = incline8(map, x, y, R, B, O)
            # R, B = data[:2]

        # else:
            # continue
        # print("-------------")
        

        if O == R and R != B:
            result.append(count)
            count -= 2
            continue

        last = (x, y)
        visited = list(visited)
        visited.append( (R, B) )
        visited = set( visited )

        count += 1
        if r == -1 or count > 10:
            count -= 2
            continue

        for i in range(4):
            data = isPossible(map, R, B, O, visited, dx[i], dy[i], last)
            print("\n@@@@@@@@")
            print(data[:2], dq, sep="\n")
            print("@@@@@@@@\n")
            if data is not None and data[:2] not in dq:
                dq.append((R, B))

        print("\n\n")
        print(x, y, dq, visited, result, sep="\t")
        printBoard(map)
        print("\n\n")

        if r == 1:
            break

    return min(result) if result!=[] else -1

def incline8(map, dx, dy, R, B, O):
    global N
    global M
    global next_goal

    iter1, iter2 = None, None

    h, v = False, False

    R2, B2 = R, B

    drc = None
    if dy == -1:
        iter1 = range(1, N)
        iter2 = range(1, M-1)
        v = True
        drc = "↑"
    elif dy == 1:
        iter1 = range(N-1, -1, -1)
        iter2 = range(1, M-1)
        v = True
        drc = "↓"
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M)
        h = True
        drc = "←"
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(M-1, -1, -1)
        h = True
        drc = "→"

    print(drc)

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

            if l == goal and now == ".":
                next_goal = c

            if prv in ["#", "R", "B"] and now in [".", "O"]:
                goal = c

            elif now == "R" and goal and prv in [".", "O"]:
                if prv == "O":
                    R = O
                    continue
                
                map[goal[1]][goal[0]] = now
                map[c[1]][c[0]] = "."

                R = goal

                goal = next_goal

            elif now == "B" and goal and prv in [".", "O"]:
                if prv == "O":
                    B = O
                    continue

                map[goal[1]][goal[0]] = now
                map[c[1]][c[0]] = "."
                B = goal

                goal = next_goal
                
        # print("\n\n")
        # break


    map[R[1]][R[0]] = "."
    map[B[1]][B[0]] = "."

    map[R2[1]][R2[0]] = "R"
    map[B2[1]][B2[0]] = "B"

    map[O[1]][O[0]] = "O"

    return R, B, O

def incline7(dx, dy):
    global data
    global N
    global M
    global R
    global B
    global O
    global next_goal

    iter1, iter2 = None, None

    h, v = False, False

    drc = None
    if dy == -1:
        iter1 = range(1, N)
        iter2 = range(1, M-1)
        v = True
        drc = "↑"
    elif dy == 1:
        iter1 = range(N-1, -1, -1)
        iter2 = range(1, M-1)
        v = True
        drc = "↓"
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M)
        h = True
        drc = "←"
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(M-1, -1, -1)
        h = True
        drc = "→"

    print(drc)

    if v:
        iter1, iter2 = iter2, iter1

    for i in iter1:
        l, c = None, None
        prv, now = None, None

        goal, hole = None, None

        for j in iter2:
            l = c

            if v:
                c = (i, j)
            else:
                c = (j, i)

            if l:
                prv = data[l[1]][l[0]]
            now = data[c[1]][c[0]]

            if l == goal and now == ".":
                next_goal = c

            if prv in ["#", "R", "B"] and now in [".", "O"]:
                goal = c
                if now == "O":
                    hole = c

            elif now == "R" and goal and prv in [".", "O"]:
                if prv == "O":
                    R = O
                    continue
                
                data[goal[1]][goal[0]] = now
                data[c[1]][c[0]] = "."

                R = goal

                goal = next_goal

            elif now == "B" and goal and prv in [".", "O"]:
                if prv == "O":
                    B = O
                    continue

                data[goal[1]][goal[0]] = now
                data[c[1]][c[0]] = "."
                B = goal

                goal = next_goal
                
        # print("\n\n")
        # break

    if O == R and R != B:
        return 1

    return 0

def incline6(dx, dy):
    global data
    global N
    global M

    global R
    global B
    global O
    global next_goal

    iter1, iter2 = None, None

    h, v = False, False

    if dy == -1:
        iter1 = range(1, M-1)
        iter2 = range(1, N)
        v = True
        print("↑"*10)
    elif dy == 1:
        iter1 = range(1, M-1)
        iter2 = range(N-1, -1, -1)
        v = True
        print("↓"*10)
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M)
        h = True
        print("←"*10)
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(M-1, -1, -1)
        h = True
        print("→"*10)

    for i in iter1:
        # if "R" not in data[i] and "B" not in data[i]:
        #     continue
        l, c = None, None
        prv, now = None, None

        hole = None

        for j in iter2:
            l = c
            if h:
                c = (i, j)
            elif v:
                c = (j, i)

            if l:
                prv = data[l[0]][l[1]]
            now = data[c[0]][c[1]]

            print(dx, dy)
            print(f"l : {l}\tc : {c}\tprv : {prv}\tnow : {now}\ti : {i}\tj : {j}")
            printBoard(data)

            # if l:
            #     print(f"l : {l}\tdata[l[0]][l[1]]:{data[l[0]][l[1]]}")
            #     print(f"now : {c}\tdata[c[0]][c[1]]:{data[c[0]][c[1]]}\n")

            if prv in [".", "O"] and now in ["R", "B"]:
                data[l[0]][l[1]], data[c[0]][c[1]] = data[c[0]][c[1]], data[l[0]][l[1]]

            """
            if now == "R":
                data[goal[0]][goal[1]] = now
                data[c[0]][c[1]] = "."
                goal = next_goal
                
                R = (goal[0], goal[1])

            elif now == "B":
                data[goal[0]][goal[1]] = now
                data[c[0]][c[1]] = "."
                goal = next_goal
                
                B = (goal[0], goal[1])
            """
        print("\n\n")
        # break

    if hole and hole == R and R != B:
        return 1

    return 0

def incline5(dx, dy):
    global data
    global N
    global M
    global R
    global B
    global O
    global next_goal

    iter1, iter2 = None, None

    h, v = False, False

    drc = None
    if dy == -1:
        iter1 = range(1, M-1)
        iter2 = range(1, N)
        v = True
        drc = "↑"
    elif dy == 1:
        iter1 = range(1, M-1)
        iter2 = range(N-1, -1, -1)
        v = True
        drc = "↓"
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M)
        h = True
        drc = "←"
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(M-1, -1, -1)
        h = True
        drc = "→"

    print(drc)

    for i in iter1:
        l, c = None, None
        prv, now = None, None

        goal, hole = None, None

        for j in iter2:
            l = c
            if h:
                c = (i, j)
            elif v:
                c = (j, i)

            if l:
                prv = data[l[0]][l[1]]
            now = data[c[0]][c[1]]



            if l == goal and now == ".":
                next_goal = c

            if prv in ["#", "R", "B"] and now in [".", "O"]:
                goal = c
                if now == "O":
                    hole = c

            elif now == "R" and goal and prv in [".", "O"]:
                if prv == "O":
                    R = O
                    continue
                
                data[goal[0]][goal[1]] = now
                data[c[0]][c[1]] = "."
                if h:
                    R = (goal[0], goal[1])
                    # R = (goal[1], goal[0])
                elif v:
                    R = (goal[1], goal[0])
                    # R = (goal[0], goal[1])

                goal = next_goal

            elif now == "B" and goal and prv in [".", "O"]:
                if prv == "O":
                    B = O
                    continue

                data[goal[0]][goal[1]] = now
                data[c[0]][c[1]] = "."
                if h:
                    B = (goal[0], goal[1])
                elif v:
                    B = (goal[1], goal[0])

                goal = next_goal
                
        # print("\n\n")
        # break

    if O == R and R != B:
        return 1

    return 0

def incline4(dx, dy):
    global data
    global N
    global M
    global last
    global R
    global B
    global O

    iter1, iter2 = None, None

    h, v = False, False

    if dy == -1:
        iter1 = range(1, M-1)
        iter2 = range(N-2, 0, -1)
        v = True
    elif dy == 1:
        iter1 = range(1, M-1)
        iter2 = range(1, N-1)
        v = True
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M-2, 0, -1)
        h = True
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(1, M-1)
        h = True

    before = (R, B)

    for i in iter1:
        l, c = (0, 0), (0, 0)

        if R and B:
            break

        for j in iter2:
            l = c
            if h:
                c = (i, j)
            elif v:
                c = (j, i)

            now = data[c[0]][c[1]]

            if data[l[0]][l[1]] == "R":
                if now == "#" or now == "B":
                    R = c

                elif now == "O":
                    R, O = c, c

                    if B:
                        return 0
                    else:
                        return 1

                elif now == ".":
                    data[c[0]][c[1]] = "R"
                    data[l[0]][l[1]] = "."
            
            elif data[l[0]][l[1]] == "B":
                if now == "O":
                    return 1

                elif now == "#" or now == "R":
                    B = c

                elif now == ".":
                    data[c[0]][c[1]] = "B"
                    data[l[0]][l[1]] = "."

            if before == (R, B):
                print(f"{dx} {dy} 못움직임")
                return -1

    else:
        return 0

def incline3(dx, dy):
    global data
    global N
    global M
    global last
    global R
    global B
    global O

    iter1, iter2 = None, None

    if dy == -1:
        iter1 = range(M)
        iter2 = range(N-1, 0, -1)
    elif dy == 1:
        iter1 = range(M)
        iter2 = range(N)
    elif dx == -1:
        iter1 = range(N)
        iter2 = range(M-1, 0, -1)
    elif dx == 1:
        iter1 = range(N)
        iter2 = range(M)

    for i in iter1:
        l, c = (0, 0), (0, 0)

        if R and B:
            break

        if "R" in data[i] and "B" in data[i]:
            for j in iter2:
                l = c
                c = (i, j)

                if data[l[0]][l[1]] == "R":
                    if data[i][j] == "#" or data[i][j] == "B":
                        R = c

                    elif data[i][j] == "O":
                        R, B, O = c, c, c

                        if B:
                            return False

                    elif data[i][j] == ".":
                        data[i][j] = "R"
                        data[l[0]][l[1]] = "."
                
                elif data[l[0]][l[1]] == "B":
                    if data[i][j] == "O":
                        return True

                    elif data[i][j] == "#" or data[i][j] == "R":
                        break

                    elif data[i][j] == ".":
                        data[i][j] = "B"
                        data[l[0]][l[1]] = "."

            break

        if "R" in data[i]:
            for j in iter2:
                l = c
                c = (i, j)
                # print(f"c : {c}")

                if data[l[0]][l[1]] == "R":
                    if data[i][j] == "#" or data[i][j] == "B":
                        R = c
                        print(f"found R : {R}")
                        break

                    elif data[i][j] == "O":
                        R, O = c, c
                        return True

                    elif data[i][j] == ".":
                        data[i][j], data[l[0]][l[1]] = data[l[0]][l[1]], "."

        elif "B" in data[i]:
            for j in iter2:
                l = c
                c = (i, j)
                # print(f"c : {c}")

                if data[l[0]][l[1]] == "B":
                    if data[i][j] == "#" or data[i][j] == "R":
                        B = c
                        print(f"found B : {B}")
                        break

                    elif data[i][j] == "O":
                        B, O = c, c
                        return False

                    elif data[i][j] == ".":
                        data[i][j], data[l[0]][l[1]] = data[l[0]][l[1]], "."
    return False

def incline2(data, N, M, y, x):
    global board
    global R
    global C
    iter1, iter2 = None, None

    if y == -1:
        iter1 = range(M)
        iter2 = range(N)
    elif y == 1:
        iter1 = range(M)
        iter2 = range(N-1, 0, -1)
    elif x == -1:
        iter1 = range(N)
        iter2 = range(M)
    elif x == 1:
        iter1 = range(N)
        iter2 = range(M-1, 0, -1)

    R, B, O = None, None, None

    for i in iter1:
        l, c = (0, 0), (0, 0)

        # if R and B:
        #     break

        if "R" in data[i] and "B" in data[i]:
            for j in iter2:
                l = c
                c = (i, j)

                if data[l[0]][l[1]] == "R":
                    if data[i][j] == "#" or data[i][j] == "B":
                        R = c

                    elif data[i][j] == "O":
                        R, O = c, True

                        if B:
                            return False

                    elif data[i][j] == ".":
                        data[i][j] = "R"
                        data[l[0]][l[1]] = "."
                
                elif data[l[0]][l[1]] == "B":
                    if data[i][j] == "O":
                        return True

                    elif data[i][j] == "#" or data[i][j] == "R":
                        break

                    elif data[i][j] == ".":
                        data[i][j] = "B"
                        data[l[0]][l[1]] = "."

            break

        if "R" in data[i] or "B" in data[i]:
            RB = None
            for j in iter2:
                l = c
                c = (i, j)

                if data[l[0]][l[1]] in ["R", "B"]:
                    if data[i][j] == "#" or data[i][j] in ["R", "B"]:
                        RB = c
                        break

                    elif data[i][j] == "O":
                        if RB and data[l[0]][l[1]] == "R":
                            return False

                        else:
                            return True

                    elif data[i][j] == ".":
                        data[i][j], data[l[0]][l[1]] = data[l[0]][l[1]], "."
    return True

def incline(data, N, M):
    global board
    global R
    global C
    while data[ny][nx] == ".":
        data[ny][nx], data[last[1]][last[0]] = data[last[1]][last[0]], data[ny][nx]
        last = (i, j)