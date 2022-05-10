# 주어진 동전으로 해당 값 만들어보기

coins = [
    [10, 50, 100, 500],
    [2, 3, 5],
    [3, 5, 8],
    [2, 5, 9]
]
R = [1440, 11, 46, 74]

def cal(r, cs, dp):
    result = 0

    a = dp[r-1]
    a = 0 if a == -1 else a

    x = 1
    cal(r - (x) , cs, dp)


    for e in  [r-c-1 for c in cs]:
        result += dp[e] if dp[e]>0 else 0

    dp[r-1] = result
    
    return min(cal(r-1, cs, dp), cal(r-2, cs, dp), cal(r-3, cs, dp)) + 1


for cs, r in zip(coins, R):
    dp = [0] * r
    dp[0] = 0
    dp[1] = -1
    dp[2] = 1

    for i in range(3, r):
        cal(i, cs, dp)

    cal(r, cs, dp)

print(dp)
