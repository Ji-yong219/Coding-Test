def main():
    result = 0
    # n, m, k = [int(i) for i in input().split(" ")]
    n, m, k = map(int, input().split())
    data = [int(i) for i in input().split(" ")]
    data.sort()

    first = data[n-1]
    second = data[n-2]

    for i in range(m):
        if (i+1) % k == 0:
            result += second
        else:
            result += first

    return result

def main():
    result = 0

    n, m, k = map(int, input().split())
    data = [int(i) for i in input().split(" ")]
    data.sort()

    first = data[n-1]
    second = data[n-2]

    result = (first*k + second) * (m // (k+1)) + (first * (m % (k+1)))

    return result
