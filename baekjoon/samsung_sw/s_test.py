def permutations(arr,n):
    if n == 0:
        yield [] 
    
    for i, el in enumerate(arr):
        for p in permutations(arr[:i] + arr[i+1:], n-1):
            yield [el] + p


def solution():
    N = int( input() )
    AN = list(map(int, input().split(" ")))
    ON = list(map(int, input().split(" ")))
    
    # 우선 n개수 찾고
    # arr만들어야겠네 
    n = len(AN) - 1
    arr = list()

    for i in range(len(ON)):
        if ON[i] > 0:
            for _ in range(ON[i]):
                arr += [i]

    per = permutations(arr, n)
    
    minNum = 10e9
    maxNum = -10e9

    
    for p in per:

        temp = AN[0]
        for num, oper in zip(AN[1:], p):
            if oper == 0:
                temp += num
            elif oper == 1:
                temp -= num
            elif oper == 2:
                temp *=  num
            elif oper == 3:
                temp = int(temp / num)
                if temp < 0:
                    temp = - (abs(temp) // num)
                else:
                    temp //= num

        minNum = min(minNum, temp)
        maxNum = max(maxNum, temp)

    print(maxNum)
    print(minNum)

solution()

    