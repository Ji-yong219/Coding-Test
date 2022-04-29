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
    for e in  [r-c-1 for c in cs]:
        result += dp[e] if dp[e]>0 else 0

    dp[r-1] = result

for cs, r in zip(coins, R):
    dp = [0] * r
    dp[0] = 0
    dp[1] = -1
    dp[2] = 1

    for i in range(3, r):
        cal(i, cs, dp)

    cal(r, cs, dp)

print(dp)