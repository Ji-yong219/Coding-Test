def main(gears, K, turns, indexs):
    result = 0

    for g, d in turns:
        axis = [i[:] for i in indexs]
        
        if d == 1:
            for i in range(2):
                indexs[g-1][i] -= 1

        else:
            for i in range(2):
                indexs[g-1][i] += 1

        for idx in range(g-2, -1, -1):
            d = -d
            if gears[idx][ axis[idx][1] %8 ] == gears[idx+1][ axis[idx+1][0] %8 ]:
                break
            else:
                if d == 1:
                    for i in range(2):
                        indexs[idx][i] -= 1
                else:
                    for i in range(2):
                        indexs[idx][i] += 1
                        
        for idx in range(g, 4):
            d = -d
            # 극이 같을 때
            if gears[idx-1][ axis[idx-1][1] %8 ] == gears[idx][ axis[idx][0] %8 ]:
                break
            else:
                if d == 1:
                    for i in range(2):
                        indexs[idx][i] -= 1
                else:
                    for i in range(2):
                        indexs[idx][i] += 1

    result = "".join( [str( gears[i][ (indexs[i][0]+2) %8 ]) for i in range(4)] )[::-1]
    result = int(result, 2)

    return result

if __name__ == "__main__":
    gears = [list(map(int, list(input()))) for _ in range(4)]
    K = int(input())
    turns = [tuple(map(int, input().split(" "))) for _ in range(K)]
    indexs = [[6, 2], [6, 2], [6, 2], [6, 2]]

    print( main(gears, K, turns, indexs) )
