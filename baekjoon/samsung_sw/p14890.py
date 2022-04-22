def main(N, L, S):
    result = 0

    for i in range(N):
        space = 1
        check = False

        for j in range(N):
            if j == N-1:
                if check and space == L:
                    space = 0
                    check = False
            else:
                next = S[i][j+1]
                now = S[i][j]
                diff = abs(next - now)

                if diff > 1:
                    break

                if check and space == L:
                    if next >= now:
                        space = 0
                    else:
                        space = 1
                    check = False

                if next > now:
                    if check:
                        break

                    elif space < L:
                        break

                    space = 1

                elif next < now:
                    if check:
                        break
                    check = True
                    space = 1
                else:
                    space += 1
        else:
            if not check:
                result += 1

    for i in range(N):
        space = 1
        check = False
        
        for j in range(N):
            if j == N-1:
                if check and space == L:
                    space = 0
                    check = False

            else:
                next = S[j+1][i]
                now = S[j][i]
                diff = abs(next - now)

                if diff > 1:
                    break

                if check and space == L:
                    if next >= now:
                        space = 0
                    else:
                        space = 1
                    check = False

                if next > now:
                    if check:
                        break

                    elif space < L:
                        break

                    space = 1

                elif next < now:
                    if check:
                        break
                    check = True
                    space = 1
                else:
                    space += 1
        else:
            if not check:
                result += 1

    return result

if __name__ == "__main__":
    N, L = list(map(int, input().split(" ")))
    S = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, L, S) )
