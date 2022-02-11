from collections import deque
from genericpath import exists
    
def main(N, M, paper):
    dq = deque()
    exist = deque()
    result = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for y in range(N):
        for x in range(M):
            visited = deque([(y, x)])
            dq.append(visited.copy())

            while visited:
                # y, x, visited = dq.pop()
                # visited = dq.pop()
                print(f"y : {y}, x : {x}\tvisited : {visited}")
                printBoard(N, M, tuple(visited))
                print("-"*30)
                

                # if len(visited) >= 4:
                #     # print(f"y : {y}, x : {x}\tvisited : {visited}")
                #     # printBoard(N, M, tuple(visited))
                #     # print("-"*30)
                #     print("this")
                #     print("-"*30)
                #     visited.pop()

                #     # visited.popleft()

                # for y, x in list(visited):

                before = len(visited)

                for k in range(4):
                    nx, ny = dx[k], dy[k]
                    target = ((y+ny), (x+nx))

                    if (0 <= target[0] < N ) and (0 <= target[1] < M) and target not in visited:

                        # if len(visited)==3 and (sum([paper[yy][xx] for yy,xx in tuple(visited)]) + paper[target[0]][target[1]]) < result:
                        #     continue

                        temp = visited.copy()
                        temp.append(target)

                        if set(temp) not in exist:
                            visited.append(target)
                            exist.append( set(visited) )
                            # dq.append( visited.copy() )

                            if len(visited) == 4:
                                temp = sum([paper[yy][xx] for yy,xx in tuple(visited)])
                                if result < temp:
                                    result = temp

                                visited.pop()
                                break

                if len(visited) == before:
                    y, x = visited.pop()

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
