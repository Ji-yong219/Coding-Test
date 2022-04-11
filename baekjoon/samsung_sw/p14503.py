def main(N, M, data, y, x, d):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = set()

    while True:
        # 현재 위치 청소
        visited.add((y, x))

        for _ in range(4):
            # 왼쪽 방향으로 회전
            d = 3 if d-1 < 0 else d-1

            ny = y + dy[d % 4]
            nx = x + dx[d % 4]

            # a. 청소하지 않은 빈 공간 존재한다면
            if (0 <= ny < N) and (0 <= nx < M) \
                    and data[ny][nx] == 0 and (ny, nx) not in visited:

                y, x = ny, nx
                break
            

        # b. 2a 연속 4번
        else:
            by = y + dy[(d+2) % 4]
            bx = x + dx[(d+2) % 4]

            # if back wall, quit
            if not((0 <= by < N) and (0 <= bx < M)) \
                    or data[by][bx] == 1:
                break

            # else, go back
            else:
                y, x = by, bx

    result = len(visited)

    return result

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    r, c, d = tuple(map(int, input().split(" ")))
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, M, data, r, c, d) )
