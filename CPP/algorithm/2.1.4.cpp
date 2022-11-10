#include <stdio.h>

int main(void) {
    int i = 0;
    int j = 0;
    bool is_prime_number = false;
    int result = 0;
    int n = 0;
    int m = 0;

    scanf("%d %d", &n, &m);

    for (i = n; i <= m; i++) {
        if (i < 2) {
            continue;
        }
        for (j = 2; j < i; j++) {
            if (i % j == 0) {
                is_prime_number = true;
                break;
            }
        }
        if (!is_prime_number) {
            result++;
            printf("%d ", i);
        }
        is_prime_number = false;
    }

    return 0;
}