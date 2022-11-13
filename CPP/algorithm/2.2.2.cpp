#include <stdio.h>

int main(void) {
    int number = 0;
    int max = 0;
    int order = 0;
    int i = 0;

    for (i = 1; i < 10; i++) {
        scanf("%d", &number);
        if (number > max) {
            max = number;
            order = i;
        }
    }
    printf("%d\n%d", max, order);

    return 0;
}