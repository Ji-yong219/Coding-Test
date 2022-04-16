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
                temp //= a
        
        if mx is None:
            mx, mn = temp, temp

        elif mx < temp:
            mx = temp
        elif mn > temp:
            mn = temp

    result = f"{mx}\n{mn}"

    return result

def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, el in enumerate(arr):
        for p in permutations(arr[:i] + arr[i+1:], n-1):
            result += [[el] + p]

    return result

if __name__ == "__main__":
    N = int( input() )
    AN = list(map(int, input().split(" ")))
    ON = list(map(int, input().split(" ")))

    print( main(N, AN, ON) )
