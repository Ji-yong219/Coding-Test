import math
def main(N, students, B, C):
    result = N

    for S in students:
        if S <= B:
            continue

        S -= B
        if S <= C:
            result += 1
            continue

        result += (S//C)

        S %= C
        if 0 < S <= C:
            result += 1
            continue

        result += math.ceil(S / C)
    return result

if __name__ == "__main__":
    N = int( input() )
    students = tuple(map(int, input().split(" ")))
    B, C = tuple(map(int, input().split(" ")))

    print( main(N, students, B, C) )