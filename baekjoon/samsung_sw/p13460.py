from ast import Break
from collections import deque

def printBoard(data):
    for row in data:
        for c in row:
            print(f"{c:3}", end="")
        print("\n")

def isPossible(R, B, dx, dy):
    global data
    x1, y1 = R
    x2, y2 = B
    
    nx1, ny1 = x1 + dx, y1 + dy
    nx2, ny2 = x2 + dx, y2 + dy
    if data[ny1][nx1] in [".", "O"] or data[ny2][nx2] in [".", "O"]:
        return True
    return False


def main(r, C, board):
    global data
    global N
    global M
    global last
    global R
    global B
    global O

    data, N, M = board, r, C
    R, B, O = None, None, None

    result = 1
    
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y, nx, ny, last = [None for _ in range(5)]

    # finding R & B
    for i in range(N):
        if R and B:
            break
        
        for j in range(M):
            if data[i][j] == "R":
                R = (j, i)

            elif data[i][j] == "B":
                B = (j, i)

    printBoard(data)
                
    for i in range(4):
        if isPossible(R, B, dx[i], dy[i]):
            dq.append((dx[i], dy[i]))

    while dq:
        x, y = dq.popleft()
        r = incline5(x, y)
        # if r != -1:
        #     break

        print(x, y)
        printBoard(data)
        print("\n\n")

        if r==1:
            break

        result += 1
        if r == 0 or result > 10:
            result = -1
            break


        for i in range(4):
            if (dx[i], dy[i]) == last:
                continue

            if isPossible(R, B, dx[i], dy[i]):
                dq.append((dx[i], dy[i]))

        last = (x, y)

    return result

def incline5(dx, dy):
    global data
    global N
    global M
    global R
    global B
    global O

    iter1, iter2 = None, None

    h, v = False, False

    if dy == -1:
        iter1 = range(1, M-1)
        iter2 = range(1, N)
        v = True
    elif dy == 1:
        iter1 = range(1, M-1)
        iter2 = range(N-1, -1, -1)
        v = True
    elif dx == -1:
        iter1 = range(1, N-1)
        iter2 = range(M)
        h = True
    elif dx == 1:
        iter1 = range(1, N-1)
        iter2 = range(M-1, -1, -1)
        h = True

    before = (R, B)

    for i in iter1:
        l, c = None, None

        goal, hole = None, None

        for j in iter2:
            l = c
            if h:
                c = (i, j)
            elif v:
                c = (j, i)

            now = data[c[0]][c[1]]

            if goal and data[goal[0]][goal[1]] != ".":
                goal = c

            elif l and data[l[0]][l[1]] in ["#", "R", "B"] and now in [".", "0"]:
                goal = c
                if now == "0":
                    hole = c

            elif now == "R":
                if goal:
                    data[goal[0]][goal[1]] = now
                    data[c[0]][c[1]] = "."
                    
                    R = (c[1], c[0])

            elif now == "B":
                if goal:
                    data[goal[0]][goal[1]] = now
                    data[c[0]][c[1]] = "."
                    
                    B = (c[1], c[0])

            print(dx, dy)
            print(f"l : {l}\tgoal : {goal}\tnow : {now}\tc : {c}\ti : {i}\tj : {j}")
            printBoard(data)

        if before == (R, B):
            return -1

        if hole and hole == R and R != B:
            return 0

    else:
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