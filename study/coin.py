# 주어진 동전으로 해당 값 만들어보기

coins = [
    [10, 50, 100, 500],
    [2, 3, 5],
    [3, 5, 8],
    [2, 5, 9]
]
R = [1440, 11, 46, 74]

def cal(r, cs, dp):
    if r < 1:
        return -1
    
    if dp[r] == -1:
        return -1

    elif dp[r] > 0:
        return dp[r]

    else:
        tp = []
        for c in cs:
            t = cal(r-c, cs, dp)
            if t == -1:
                continue
            tp.append(t)

        if tp == [] or min(tp) < 1:
            return -1

        else:
            dp[r] = min(tp)+1
            return min(tp) + 1


for cs, r in zip(coins, R):
    dp = [0] * (r+1)
    mn = min(cs)
    for i in range(0, mn+1):
        dp[i] = -1

    for c in cs:
        dp[c] = 1

    dp[mn] = 1

    t = cal(r, cs, dp)
    print(f"동전 {cs} 중 {r}를 만드는 최소 개수 : {t}개")