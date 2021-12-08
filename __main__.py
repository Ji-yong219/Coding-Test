from time import time
from this_is_coding_test.ex3_1 import main

if __name__ == "__main__":
    start = time()

    print(main())

    print(f"progress time : {time() - start}s")
