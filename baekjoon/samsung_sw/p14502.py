from collections import deque
from itertools import permutations

def bfs(N, M, data, viruses):
    visited = set()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for v in viruses:
        dq = deque([v])

        while dq:
            y, x = dq.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 <= ny < N) and (0 <= nx < M):
                    if data[ny][nx] == 0 and (ny, nx) not in visited:
                        visited.add((ny, nx))
                        dq.append((ny, nx))

    return len(visited)



def main(N, M, data):
    result = 0
    whole_count = 0
    viruses = []
    blanks = []

    for y in range(N):
        for x in range(M):
            if data[y][x] == 0:
                blanks.append((y, x))
                whole_count += 1

            elif data[y][x] == 2:
                viruses.append((y, x))

    walls = tuple(permutations(blanks, 3))

    for wall in walls:
        for w in wall:
            data[w[0]][w[1]] = 1
            
        result = max(result, whole_count - bfs(N, M, data, viruses))

        for w in wall:
            data[w[0]][w[1]] = 0

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, M, data) )
