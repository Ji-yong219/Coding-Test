#include <iostream>

using namespace std;

int main(void) {
    int N = 0;
    int M = 0;
    int A = 0;
    int B = 0;
    int i = 0;
    int j = 0;

    scanf("%d %d", &N, &M);

    int num_arr[N][M] = {0, };

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            cin >> num_arr[i][j];
        }
    }

    scanf("%d %d", &A, &B);

    printf("%d", num_arr[A][B]);

    return 0;
}