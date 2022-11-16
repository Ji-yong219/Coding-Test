#include <iostream>

using namespace std;

int main(void) {
    int decimal_number = 0;
    int binary_number = 0;
    int digit_value = 1;

    cin >> decimal_number;

    while (decimal_number > 0) {
        binary_number += decimal_number % 2 * digit_value;
        decimal_number /= 2;
        digit_value *= 10;
    }
    printf("%d", binary_number);

    return 0;
}