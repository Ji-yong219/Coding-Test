from datetime import datetime
# from this_is_coding_test.ex3_2 import main
from baekjoon.samsung_sw import main

if __name__ == "__main__":
    start = datetime.now()

    N = int( input() )
    data = [list(map(int, input().split(" "))) for _ in range(N)]

    print( main(N, data) )

    print(f"progress time : {datetime.now() - start}s")
