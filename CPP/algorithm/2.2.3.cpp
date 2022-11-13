#include <stdio.h>

int main(void) {
    int i = 0;
    int num = 0;
    int min_arr[2][2] = {
        {10000000, -1},
        {10000000, -1}
    };

    for (i = 1; i <= 9; i++) {
        scanf("%d", &num);

        if (num < min_arr[1][0]) {
            min_arr[1][0] = num;
            min_arr[1][1] = i;

            if (num < min_arr[0][0]) {
                min_arr[1][0] = min_arr[0][0];
                min_arr[1][1] = min_arr[0][1];

                min_arr[0][0] = num;
                min_arr[0][1] = i;
            }
        }
    }
    printf("%d\n%d", min_arr[1][0], min_arr[1][1]);

    return 0;
}