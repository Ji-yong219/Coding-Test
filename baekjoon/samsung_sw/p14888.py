def main(N, AN, ON):
    result = 0

    oo = [1] * ON[0] + [2] * ON[1] + [3] * ON[2] + [4] * ON[3]
    operators = permutations(oo, N-1)

    mx = None
    mn = None
    for operator in operators:
        temp = AN[0]
        for a, o in zip(AN[1:], operator):
            if o == 1:
                temp += a
            elif o == 2:
                temp -= a
            elif o == 3:
                temp *= a
            elif o == 4:
                if temp < 0:
                    temp = - (abs(temp) // a)
                else:
                    temp //= a
        
        if mx is None:
            mx, mn = temp, temp

        if mx < temp:
            mx = temp
        if mn > temp:
            mn = temp
        
    result = f"{mx}\n{mn}"

    return result

def permutations(arr, n):
    if n == 0:
        yield [[]]

    for i, el in enumerate(arr):
        for p in permutations(arr[ :i] + arr[i+1: ], n-1):
            yield [el] + p

if __name__ == "__main__":
    N = int( input() )
    AN = list(map(int, input().split(" ")))
    ON = list(map(int, input().split(" ")))

    print( main(N, AN, ON) )
