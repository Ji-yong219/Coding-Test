from collections import deque
    
def main(N, apple_data, direction_data):
    dq = deque()
    dd = ((1, 0), (0, 1), (-1, 0), (0, -1))
    idx, sec, y, x = 0, 0 ,0, 0

    while True:
        sec += 1

        dq.append((y, x))

        x += dd[idx][0]
        y += dd[idx][1]

        if not (-1 < y < N) or not (-1 < x < N) or (y, x) in dq:
            break

        elif (y+1, x+1) in apple_data:
            del apple_data[ apple_data.index((y+1, x+1)) ]
        
        else:
            dq.popleft()
        
        if direction_data and sec == int(direction_data[0][0]):
            _, d = direction_data.pop(0)

            if d == "L":
                idx = (idx-1) % 4

            elif d == "D":
                idx = (idx+1) % 4

    return sec

if __name__ == "__main__":
    N = int( input() )
    AN = int( input() )
    apple_data = [tuple(map(int, input().split(" "))) for _ in range(AN)]
    DN = int( input() )
    direction_data = [input().split(" ") for _ in range(DN)]

    print( main(N, apple_data, direction_data) )