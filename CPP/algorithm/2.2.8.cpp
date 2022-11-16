#include <iostream>

using namespace std;

int main(void) {
    int N = 0;
    int S = 0;
    int i = 0;
    int j = 0;
    int k = 0;
    int blank_count = 0;
    int total_count = 0;
    int increase_number = 0;
    int decrease_number = 0;

    scanf("%d %d", &N, &S);
    total_count = (N * 2) - 1;
    increase_number = S;

    for (i = 1; i <= N; i++) {
        blank_count = total_count - (i * 2) + 1;
        for (j = 0; j < blank_count / 2; j++) {
            printf("%3c", ' ');
        }
        
        if (i % 2 == 1) {
            decrease_number = increase_number + total_count - blank_count - 1;
            if (decrease_number > 9) {
                decrease_number %= 9;
            }
            increase_number = decrease_number + 1;
            
            for (k = 0; k < total_count - blank_count; k++) {
                printf("%3d", decrease_number);

                decrease_number--;
                if (decrease_number < 1) {
                    decrease_number = 9;
                }
            }
        } else {
            for (k = 0; k < total_count - blank_count; k++) {
                printf("%3d", increase_number);

                increase_number++;
                if (increase_number > 9) {
                    increase_number = 1;
                }
            }
        }
        
        for (j = 0; j < blank_count / 2; j++) {
            printf("%3c", ' ');
        }
        printf("\n");
    }

    return 0;
}