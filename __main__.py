from datetime import datetime
from this_is_coding_test.ex3_2 import main

if __name__ == "__main__":
    start = datetime.now()

    print(main())

    print(f"progress time : {datetime.now() - start}s")
