def main(N, S):
    result = 10e8

    temp = [i for i in range(1, N+1)]
    com = combinations(temp, N//2)
    temp = set(temp)

    for start in com:
        link = list( temp - set(start) )

        sum_start = 0
        for i, j in combinations(start, 2):
            sum_start += S[i-1][j-1]
            sum_start += S[j-1][i-1]

        sum_link = 0
        for i, j in combinations(link, 2):
            sum_link += S[i-1][j-1]
            sum_link += S[j-1][i-1]

        r = abs(sum_start - sum_link)
        if r < result:
            result = r

        if result == 0:
            break

    return result

def combinations(arr, n):
    if n == 0:
        return [[]]

    result = []
    for i, el in enumerate(arr):
        for c in combinations( arr[i+1: ], n-1):
            result += ([el] + c,)
    return result

if __name__ == "__main__":
    N = int( input() )
    S = [ list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, S) )
