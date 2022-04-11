from collections import deque

def bfs(N, M, data, viruses):
    visited = []

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
                        visited.append((ny, nx))
                        dq.append((ny, nx))

    return len(visited)



def main(N, M, data):
    result = 0
    whole_count = 0
    viruses = []
    walls = []

    for y in range(N):
        for x in range(M):
            if data[y][x] == 0:
                # if len(walls) < 3:
                #     walls.append((y, x))
                #     data[y][x] = 1
                # else:
                whole_count += 1

            elif data[y][x] == 2:
                viruses.append((y, x))

    result = whole_count - bfs(N, M, data, viruses)

    print(whole_count, result)

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, M, data) )
