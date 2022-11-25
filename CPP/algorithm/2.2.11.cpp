#include <iostream>

using namespace std;

int main(void) {
    int N = 0;
    int i = 0;
    int j = 0;

    int prev_num1 = 1;
    int prev_num2 = 0;

    cin >> N;

    for (i = 0; i < N; i++) {
        for (j = 0; j < N - i; j++) {
            printf("%d ", j + prev_num1 + prev_num2 );
            prev_num1 = j + prev_num1 + prev_num2;
        }
        prev_num1 = prev_num1 - j;
        prev_num2 += prev_num1 + i;
        printf("\n");
    }

    return 0;
}