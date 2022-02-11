from collections import deque
    
def main(N, M, paper):
    dq = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    exists = deque()
    result = 0

    visited = [(0, 0), (0, 1), (0, 2), (0, 3)]
    dq.append((0, 3, deque( visited )))

    while dq:
        y, x, visited = dq.popleft()

        if len(visited) >= 4:
            temp = sum([paper[y][x] for y,x in tuple(visited)])
            if result < temp:
                result = temp

            visited = deque([(y, x)])

        for y, x in list(visited):
            for k in range(4):
                nx, ny = dx[k], dy[k]
                target = ((y+ny), (x+nx))

                if (0 <= (y+ny) < N ) and (0 <= (x+nx) < M) and len(visited) < 4 and target not in visited:
                    visited.append(target)
                    if set(visited) not in exists:
                        dq.append( (target[0], target[1], visited.copy()) )
                        exists.append( set(visited) )
                    
                    visited.pop()

    return result

if __name__ == "__main__":
    N, M = tuple( map(int, input().split(" ") ) )
    paper = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, M, paper) )