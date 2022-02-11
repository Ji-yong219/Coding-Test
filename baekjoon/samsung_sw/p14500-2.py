from collections import deque
    
def main(N, M, paper):
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    exists = deque()
    result = 0

    dq.append((0, 0, deque( {(0, 0)} )))
    visited = deque({(0, 0)})

    while dq:
        y, x, visited = dq.popleft()

        if len(visited) >= 4:
            print(f"y : {y}, x : {x}\tvisited : {visited}")
            printBoard(N, M, tuple(visited))
            print("-"*30)
            temp = sum([paper[yy][xx] for yy,xx in tuple(visited)])
            if result < temp:
                result = temp

            visited.popleft()

        for k in range(4):
            nx, ny = dx[k], dy[k]
            target = ((y+ny), (x+nx))

            if (0 <= target[0] < N ) and (0 <= target[1] < M) and target not in visited and len(visited) < 4:
                visited.append(target)
                if set(visited) not in exists:
                    dq.append( (target[0], target[1], visited.copy()) )
                    exists.append( set(visited) )

                    if len(visited) >= 4:
                        visited.pop()

    return result

def printBoard(N, M, nyx):
    for yy in range(N):
        for xx in range(M):
            if (yy, xx) in nyx:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()

if __name__ == "__main__":
    N, M = tuple( map(int, input().split(" ") ) )
    paper = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, paper) )