#include <iostream>

using namespace std;

int main(void) {
    int numbercard_arr_of_A[10] = {0, };
    int numbercard_arr_of_B[10] = {0, };
    int i = 0;
    int count_of_victory_arr[2] = {0, 0};

    for (i = 0; i < 10; i++) {
        cin >> numbercard_arr_of_A[i];
    }

    for (i = 0; i < 10; i++) {
        cin >> numbercard_arr_of_B[i];
    }

    for (i = 0; i < 10; i++) {
        if (numbercard_arr_of_A[i] > numbercard_arr_of_B[i]) {
            count_of_victory_arr[0]++;
        } else if (numbercard_arr_of_A[i] < numbercard_arr_of_B[i]) {
            count_of_victory_arr[1]++;
        }
    }

    if (count_of_victory_arr[0] > count_of_victory_arr[1]) {
        printf("A");
    } else if (count_of_victory_arr[1] > count_of_victory_arr[0]) {
        printf("B");
    } else {
        printf("D");
    }

    return 0;
}