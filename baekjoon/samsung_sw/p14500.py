from collections import deque
    
def main(N, M, paper):
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    exists = []
    visited = set()
    result = 0

    visited.add((0, 0))

    for i in range(N):
        for j in range(M):
            dq.append((i, j, {(i, j)}))
            visited = set()

            while dq:
                y, x, visited = dq.popleft()

                if len(visited) >= 4:
                    exists.append( visited )
                    temp = sum([paper[y][x] for y,x in tuple(visited)])
                    if result < temp:
                        result = temp

                    visited = set()
                    continue

                for k in range(4):
                    nx, ny = dx[k], dy[k]
                    target = ((y+ny), (x+nx))

                    if (0 <= (y+ny) < N ) and (0 <= (x+nx) < M) and target not in visited:
                        temp = visited.copy()
                        temp.add(target)

                        if  temp not in exists:
                            visited.add( target )
                            dq.append( (target[0], target[1], visited.copy()) )

    for r in exists:
        print(r)
    return result

if __name__ == "__main__":
    N, M = tuple( map(int, input().split(" ") ) )
    paper = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, paper) )