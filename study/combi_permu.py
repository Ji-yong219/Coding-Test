def permutations(arr, n):
    if n == 0 :
        return [[]]

    result = []

    for i, el in enumerate(arr):
        for p in permutations(arr[:i] + arr[i+1:], n-1):
            result += [[el] + p]
    return result

def combinations(arr, n):
    if n == 0 :
        # return [[]]
        yield []

    for i, el in enumerate(arr):
        for c in combinations(arr[:i], n-1):
            # result += [[el] + c] #append
            # result.append([el] + c)
            yield [el] + c

arr = [1,2,3,4,5]
n = 2
print("원본 : ", arr)
# print("순열 : ", permutations(arr, n))
print("조합 : ", combinations(arr, n))


# for i in range(100000000000000000000000):
#     break

for com in combinations(arr, n):
    com + a