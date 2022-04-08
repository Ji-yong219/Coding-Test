def main(N, plan):
    result = 0
    
    cost = []

    for i in range(N):
        for j in range(i):
            print(i, j)

    return result

if __name__ == "__main__":
    N = int(input())
    plan = [ tuple(map(int, input().split(" "))) for _ in range(N) ]
    print( main(N, plan) )
