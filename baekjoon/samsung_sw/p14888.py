def main(N, data):
    # result = 0
    a = permutations([1,2,3,], 2)
    print(a)

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
    data = [ list(map(int, input().split(" "))) for _ in range(N) ]

    print( main(N, data) )
