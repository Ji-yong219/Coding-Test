def main(gears, K, turns, indexs):
    result = 0

    for g, d in turns:
        # print(gears)
        # print(indexs)
        # print(g, d)
        if d:
            for i in range(2):
                indexs[g-1][i] += 1

        else:
            for i in range(2):
                indexs[g-1][i] -= 1

        # print("↓")

        # print(gears)
        # print(indexs)
        # print(g, d)
        # break

        for idx in range(g-1, -1, -1):
            # 극이 같을 때
            if gears[idx][ indexs[idx][1] %8 ] == gears[idx+1][ indexs[idx+1][0] %8 ]:
                break
            else:
                if d:
                    for i in range(2):
                        indexs[idx][i] -= 1
                else:
                    for i in range(2):
                        indexs[idx][i] += 1
                        
        for idx in range(g+1, 4):
            # 극이 같을 때
            if gears[idx][ indexs[idx][1] %8 ] == gears[idx-1][ indexs[idx-1][0] %8 ]:
                break
            else:
                if d:
                    for i in range(2):
                        indexs[idx][i] -= 1
                else:
                    for i in range(2):
                        indexs[idx][i] += 1

        for idx in range(4):
            v = gears[idx][ (indexs[idx][0]+2) %8 ]
            if v == 0:
                if idx == 0:
                    result += 1
                elif idx == 1:
                    result += 2
                elif idx == 2:
                    result += 4
                elif idx == 3:
                    result += 8

    # for g, i in zip(gears, indexs):
    #     print(g, i)

    return result

if __name__ == "__main__":
    gears = [list(map(int, list(input()))) for _ in range(4)]
    K = int(input())
    turns = [tuple(map(int, input().split(" "))) for _ in range(K)]
    indexs = [[6, 2], [6, 2], [6, 2], [6, 2]]

    print( main(gears, K, turns, indexs) )
