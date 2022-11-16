#include <iostream>

using namespace std;

int main(void) {
    int N = 0;
    int M = 0;

    int i = 0;
    int j = 0;

    scanf("%d %d", &N, &M);

    int number_array[N][M] = {0, };
    int increase_number = 1;

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            number_array[i][j] = increase_number;
            increase_number++;
        }
    }
    

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            printf("%3d", number_array[i][j]);
        }
        printf("\n");
    }

    return 0;
}