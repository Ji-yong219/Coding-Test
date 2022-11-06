#include <stdio.h>

int main(void) {
    int i = 0;
    int j = 0;
    int count = 0;
    int star_cnt = 0;

    printf("input : ");
    scanf("%d, &count");

    for (i = 1, star_cnt = 1; i <= count; i++, star_cnt += 2) {
        for (j = count - star_cnt; j > 0; j--) {
            printf(" ");
        }

        for (j = 0; j < star_cnt; j++) {
            printf("*");
        }

        printf("\n");
    }
}